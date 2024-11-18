from rest_framework import serializers
from patient.models import MedicalHistory


class MedicalHistoryListSerializer(serializers.Serializer):
    patient = serializers.CharField()
    allergy = serializers.CharField()
    notes = serializers.CharField()


class MedicalHistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'


class MedicalHistoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'


class MedicalHistoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ['allergy', 'notes']


class MedicalHistoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = '__all__'
