from analytic.models import Department
from doctor.models import Doctor
from patient.models import Patient
from service.models import Service
from django.db.models import Sum, Count, Avg, F, ExpressionWrapper, DurationField
from visit.models import Visit
from django.db.models.functions import Now


def doctor_all_count():
    return Doctor.objects.all().count()


def patient_all_count():
    return Patient.objects.all().count()


def get_total_sum_income():
    return Visit.objects.aggregate(total_income=Sum('service__price'))['total_income'] or 0


def get_total_expenses():
    return Service.objects.aggregate(total_expenses=Sum('price'))['total_expenses'] or 0


def get_total_profit():
    return get_total_sum_income() - get_total_expenses()


def get_department_info():
    departments = Department.objects.prefetch_related('doctors').annotate(doctor_count=Count('doctors'))
    department_data = []

    for department in departments:
        doctors_info = [doctor.full_name for doctor in department.doctors.all()]
        
        if not doctors_info:
            doctors_info = ['На данный момент нет врача в этом отделений']
        
        department_data.append({
            'department_name': department.name,
            'doctor_count': department.doctor_count,
            'doctors': doctors_info
        })
    return department_data


def get_department_avg_rating():
    departments = Department.objects.annotate(avg_rating=Avg('doctors__visits__rating')).prefetch_related(
        'doctors__visits'
    )
    department_data = []

    for department in departments:
        avg_rating = department.avg_rating if department.avg_rating is not None else 'Нет рейтингов'

        department_data.append({
            'department_name': department.name,
            'avg_rating': avg_rating
        })
    return department_data


def get_avg_treatment_time():
    completed_visits = Visit.objects.filter(status=Visit.COMPLETED, end_date_time__isnull=False)

    if not completed_visits.exists():
        return None

    treatment_times = completed_visits.annotate(
        treatment_duration=ExpressionWrapper(
            F('end_date_time') - F('visit_date_time'),
            output_field=DurationField()
        )
    )

    avg_duration = treatment_times.aggregate(
        avg_duration=Avg('treatment_duration')
    )['avg_duration']

    if avg_duration is None:
        return None

    return str(avg_duration)