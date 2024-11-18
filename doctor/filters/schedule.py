import django_filters as filters
from doctor.models import Schedule


class ScheduleFilterSet(filters.FilterSet):
    day_of_week = filters.ChoiceFilter()

    class Meta:
        model = Schedule
        fields = '__all__'

    