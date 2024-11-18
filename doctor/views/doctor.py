from rest_framework import mixins, viewsets
from rest_framework.response import Response
from doctor.filters.doctor import DoctorFilterSet
from doctor.models import Doctor
from doctor.serializers.doctor import DoctorListSerializer, DoctorCreateSerializer, DoctorRetrieveSerializer, \
    DoctorUpdateSerializer, DoctorDeleteSerializer
from patient.models import Patient
from patient.serializers import PatientListSerializer
from rest_framework.permissions import IsAuthenticated
from doctor.permissions.doctor import DoctorAccessPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class DoctorView(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin
                 ):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = DoctorListSerializer
    search_fields = ['first_name', 'last_name', 'specialization__name']
    ordering_fields = ['first_name', 'last_name', 'specialization__name']
    ordering = ['first_name']
    permission_classes = [IsAuthenticated, DoctorAccessPermission]
    filterset_class = DoctorFilterSet

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'destroy':
            return DoctorDeleteSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.all()
        return Doctor.objects.all()

    def list_patient(self, request, pk):
        queryset = self.get_queryset().filter(visits__doctor_id=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)