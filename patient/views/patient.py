from patient.models import Patient
from rest_framework import mixins, viewsets
from patient.serializers import PatientListSerializer, PatientRetrieveSerializer, PatientCreateSerializer, \
    PatientDeleteSerializer, PatientUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from patient.permissions import PatientAccessPermission
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from patient.filters.patient import PatientFilterSet


class PatientView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = PatientListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'gender', 'age']
    ordering_fields = ['first_name', 'gender']
    ordering = ['first_name']
    permission_classes = [IsAuthenticated, PatientAccessPermission]
    filterset_class = PatientFilterSet

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'create':
            return PatientCreateSerializer
        if self.action == 'retrieve':
            return PatientRetrieveSerializer
        if self.action == 'update':
            return PatientUpdateSerializer
        if self.action == 'destroy':
            return PatientDeleteSerializer

    def get_queryset(self):
        return Patient.objects.all()