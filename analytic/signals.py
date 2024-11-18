from django.utils import timezone
from doctor.models import Doctor, Schedule
from patient.models import Patient
from visit.models import Visit
from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver
from analytic.models import Notification


@receiver(post_save, sender=Visit)
def notify_on_new_visit(sender, instance, created, **kwargs):
    if created:
        schedule = Schedule.objects.filter(doctor=instance.doctor, start_time__lte=instance.visit_date_time,
                                           end_time__gte=instance.visit_date_time).first()
        if schedule:
            Notification.objects.create(
                sender=instance.patient.user,
                recipient=instance.doctor.user,
                message=f"Новый визит запланирован на {instance.visit_date_time}.",
                notification_type=Notification.VISIT_CREATED
            )


@receiver(post_save, sender=Visit)
def notify_on_cancelled_visit(sender, instance, **kwargs):
    if instance.status == Visit.CANCELLED:
        schedule = Schedule.objects.filter(doctor=instance.doctor, start_time__lte=instance.visit_date_time,
                                           end_time__gte=instance.visit_date_time).first()
        if schedule:
            Notification.objects.create(
                sender=instance.patient.user,
                recipient=instance.doctor.user,
                message="Визит отменен",
                notification_type=Notification.VISIT_CANCELLED
            )


@receiver(pre_delete, sender=Doctor)
def notify_on_doctor_delete(sender, instance, **kwargs):
    upcoming_visits_users_id = Visit.objects.filter(
        doctor=instance,
        visit_date_time__gte=timezone.now()
    ).values_list('patient__user_id', flat=True)

    for user_id in upcoming_visits_users_id:
        Notification.objects.create(
            sender=instance.user,
            recipient_id=user_id,
            message=f"Врач {instance.full_name} удален, все связанные визиты и расписания также удалены",
            notification_type=Notification.DOCTOR_DELETE
        )


@receiver(pre_delete, sender=Patient)
def delete_related_visits(sender, instance, **kwargs):
    related_visits = Visit.objects.filter(patient=instance)
    for visit in related_visits:
        schedule = Schedule.objects.filter(doctor=visit.doctor, start_time__lte=visit.visit_date_time,
                                           end_time__gte=visit.visit_date_time).first()
        if schedule:
            Notification.objects.create(
                sender=instance.user,
                recipient=visit.doctor.user,
                message=f"Пациент {instance.full_name} удален, связанный визит также удален",
                notification_type=Notification.PATIENT_DELETE
            )