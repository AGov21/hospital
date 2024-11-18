from patient.models import MedicalHistory
from rest_framework import mixins, viewsets
from patient.serializers.medical_history import MedicalHistoryListSerializer, MedicalHistoryCreateSerializer, \
    MedicalHistoryUpdateSerializer, MedicalHistoryRetrieveSerializer, MedicalHistoryDeleteSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from patient.permissions import MedicalHistoryAccessPermission


class MedicalHistoryView(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    serializer_class = MedicalHistoryListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['patient', 'allergy']
    permission_classes = [IsAuthenticated, MedicalHistoryAccessPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return MedicalHistoryListSerializer
        if self.action == 'create':
            return MedicalHistoryCreateSerializer
        if self.action == 'retrieve':
            return MedicalHistoryRetrieveSerializer
        if self.action == 'update':
            return MedicalHistoryUpdateSerializer
        if self.action == 'destroy':
            return MedicalHistoryDeleteSerializer

    def get_queryset(self):
        return MedicalHistory.objects.all()