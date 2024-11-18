from rest_framework import mixins, viewsets
from specialization.models import Specialization
from specialization.serializers import SpecializationListSerializer, SpecializationRetrieveSerializer, \
    SpecializationUpdateSerializer, SpecializationDeleteSerializer, SpecializationCreateSerializer

from rest_framework.permissions import IsAuthenticated
from specialization.permissions import SpecializationAccessPermission
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class SpecializationView(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    serializer_class = SpecializationListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['^name']


    permission_classes = [IsAuthenticated, SpecializationAccessPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return SpecializationListSerializer
        if self.action == 'create':
            return SpecializationCreateSerializer
        if self.action == 'retrieve':
            return SpecializationRetrieveSerializer
        if self.action == 'update':
            return SpecializationUpdateSerializer
        if self.action == 'destroy':
            return SpecializationDeleteSerializer

    def get_queryset(self):
        return Specialization.objects.all()