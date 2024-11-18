from rest_framework import serializers


class FinancialPerformanceSerializer(serializers.Serializer):
    total_income = serializers.FloatField()
    total_expenses = serializers.FloatField()
    total_profit = serializers.FloatField()


class DepartmentListSerializer(serializers.Serializer):
    department_name = serializers.CharField()
    doctor_count = serializers.IntegerField()
    doctors = serializers.ListField(child=serializers.CharField())



class AvgRatingSerializer(serializers.Serializer):
    department_name = serializers.CharField()
    avg_rating = serializers.FloatField()


class AnalyticsSerializer(serializers.Serializer):
    doctor_count = serializers.IntegerField()
    patient_count = serializers.IntegerField()
    financial_performance = FinancialPerformanceSerializer()
    departments_info = DepartmentListSerializer(many=True)
    avg_rating_department = AvgRatingSerializer(many=True)
    avg_treatment_time = serializers.DurationField()