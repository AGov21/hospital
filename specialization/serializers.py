from specialization.models import Specialization
from rest_framework import serializers


class SpecializationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SpecializationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SpecializationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SpecializationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['name']


class SpecializationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'