import django_filters as filters
from visit.models import Visit


class VisitFilterSet(filters.FilterSet):
    visit_date_time = filters.DateTimeFromToRangeFilter(field_name='visit_date_time')


    class Meta:
        model = Visit
        fields = ['doctor', 'patient', 'service', 'visit_date_time', 'status']