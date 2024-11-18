from rest_framework import mixins, viewsets

from service.filters import ServiceFilterSet
from service.models import Service
from service.serializers import ServiceListSerializer, ServiceCreateSerializer, \
    ServiceRetrieveSerializer, ServiceUpdateSerializer, ServiceDeleteSerializer

from rest_framework.permissions import IsAuthenticated
from service.permissions import ServiceAccessPermission
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ServiceView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = ServiceListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilterSet
    permission_classes = [IsAuthenticated, ServiceAccessPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        if self.action == 'create':
            return ServiceCreateSerializer
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        if self.action == 'update':
            return ServiceUpdateSerializer
        if self.action == 'destroy':
            return ServiceDeleteSerializer

    def get_queryset(self):
        return Service.objects.all()