import django_filters as filters
from service.models import Service


class ServiceFilterSet(filters.FilterSet):
    price = filters.NumericRangeFilter(field_name='price')
    duration = filters.DurationFilter()
    min_duration = filters.DurationFilter(field_name='duration', lookup_expr='gte')
    max_duration = filters.DurationFilter(field_name='duration', lookup_expr='lte')

    class Meta:
        model = Service
        fields = ['name', 'price', 'duration', 'min_duration', 'max_duration']