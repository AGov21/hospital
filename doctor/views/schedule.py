from doctor.models import Schedule
from doctor.serializers.schedule import ScheduleListSerializer, ScheduleDeleteSerializer, \
    ScheduleCreateSerializer, ScheduleRetrieveSerializer, ScheduleUpdateSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from doctor.permissions.schedule import ScheduleAccessPermission
from doctor.filters.schedule import ScheduleFilterSet
from django_filters.rest_framework import DjangoFilterBackend


class ScheduleView(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated, ScheduleAccessPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScheduleFilterSet

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        if self.action == 'create':
            return ScheduleCreateSerializer
        if self.action == 'retrieve':
            return ScheduleRetrieveSerializer
        if self.action == 'update':
            return ScheduleUpdateSerializer
        if self.action == 'destroy':
            return ScheduleDeleteSerializer

    def get_queryset(self):
        return Schedule.objects.all()