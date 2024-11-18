from rest_framework import mixins, viewsets
from rest_framework.response import Response
from visit.filters import VisitFilterSet
from visit.models import Visit
from visit.serializers import VisitListSerializer, VisitDeleteSerializer, VisitRetrieveSerializer, \
    VisitUpdateSerializer, VisitCreateSerializer, VisitRatingSerializer
from rest_framework.permissions import IsAuthenticated
from visit.permissions import VisitAccessPermission
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status


class VisitView(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin):
    serializer_class = VisitListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^doctor__first_name', '^patient__first_name', '=service__name', 'visit_date_time']
    ordering_fields = ['doctor', 'patient', 'service', 'visit_date_time', 'status']
    ordering = ['doctor']
    permission_classes = [IsAuthenticated, VisitAccessPermission]
    filterset_class = VisitFilterSet

    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'update':
            return VisitUpdateSerializer
        if self.action == 'destroy':
            return VisitDeleteSerializer
        if self.action == 'set_rating':
            return VisitRatingSerializer

    def get_queryset(self):
        return Visit.objects.all()

    def set_rating(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)