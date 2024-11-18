import django_filters as filters
from patient.models import Patient


class PatientFilterSet(filters.FilterSet):
    date_of_birth = filters.DateFromToRangeFilter()

    class Meta:
        model = Patient
        fields = '__all__'