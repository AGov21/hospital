import django_filters as filters
from doctor.models import Doctor


class DoctorFilterSet(filters.FilterSet):
    specialization = filters.CharFilter()

    class Meta:
        model = Doctor
        fields = {
            'first_name': ['exact', 'contains'],
            'last_name': ['exact', 'contains'],
        }

    
