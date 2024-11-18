from rest_framework import serializers
from doctor.models import Doctor


class DoctorListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    specialization = serializers.CharField()
    full_name = serializers.CharField()
    contact_info = serializers.CharField()


class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'contact_info']


class DoctorDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
