from rest_framework import viewsets, mixins
from analytic.analytics import get_total_expenses, get_total_sum_income, doctor_all_count, patient_all_count, \
    get_total_profit, get_department_info, get_department_avg_rating, get_avg_treatment_time
from rest_framework.response import Response
from analytic.serializers import AnalyticsSerializer
from rest_framework import status
from analytic.models import Department


class AnalyticsView(viewsets.GenericViewSet,
                    mixins.ListModelMixin):

    def get_serializer_class(self):
        if self.action == 'get_analytics':
            return AnalyticsSerializer

    def get_analytics(self, request):
        response = {
            'patient_count': patient_all_count(),
            'doctor_count': doctor_all_count(),
            'financial_performance': {
                'total_income': get_total_sum_income(),
                'total_expenses': get_total_expenses(),
                'total_profit': get_total_profit()

            },
            'departments_info': get_department_info(),
            'avg_rating_department': get_department_avg_rating(),
            'avg_treatment_time': get_avg_treatment_time()
        }
        return Response(status=status.HTTP_200_OK, data=response)

    def get_queryset(self):
        return Department.objects.all()