from patient.models import Patient
from rest_framework import serializers


class PatientListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    age = serializers.IntegerField()
    date_of_birth = serializers.DateField()
    gender = serializers.CharField()
    contact_info = serializers.CharField()


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientRetrieveSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    gender = serializers.CharField()
    contact_info = serializers.CharField()
    date_of_birth = serializers.DateField()


class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['contact_info', 'date_of_birth']


class PatientDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'