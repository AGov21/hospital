from rest_framework import serializers
from doctor.models import Schedule


class ScheduleListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField(source='doctor.full_name')
    doctor_id = serializers.IntegerField()

    class Meta:
        model = Schedule
        fields = ['id', 'full_name', 'doctor_id', 'day_of_week', 'start_time', 'end_time']


class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['doctor', 'day_of_week']


class ScheduleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['day_of_week', 'start_time', 'end_time']


class ScheduleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'