from datetime import timedelta
from visit.models import Visit
from rest_framework import serializers
from django.core.exceptions import ValidationError


class VisitListSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField()
    patient = serializers.StringRelatedField()
    service = serializers.StringRelatedField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, default=0)
    visit_date_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')

    class Meta:
        model = Visit
        fields = '__all__'


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

    
    def validate(self, data):

        patient = data.get('patient')
        doctor = data.get('doctor')
        visit_start_time = data.get('visit_date_time')
        visit_end_time = visit_start_time + data.get('service').duration
        visit_day_of_week = visit_start_time.strftime('%A')  


        if not patient or not doctor:
            raise serializers.ValidationError('Пациент и врач должны быть указаны.')
        
        if patient.age >= 18 and doctor.department.name == 'Педиатрические отделения':
            raise serializers.ValidationError('Пациент должен быть младше 18 лет для записи в педиатрическое отделение.')
        
    
        if Visit.objects.filter(
            patient=patient,
            visit_date_time=visit_end_time,
            end_date_time__gte=visit_start_time
        ).exists():
            raise serializers.ValidationError('Пациент уже записан на это время.')
        
    

        existing_visit =  Visit.objects.filter(
            doctor=doctor,
            visit_date_time__lt=visit_end_time,
            end_date_time__gt=visit_start_time
        ).first()
        
        if existing_visit:
            raise serializers.ValidationError(
                f'Пациент уже записан на это время: {existing_visit.visit_date_time} - {existing_visit.end_date_time}.'
            )


        schedule = doctor.schedules.filter(
            day_of_week=visit_day_of_week
        ).first()

        if not schedule:
            raise serializers.ValidationError(f'Врач не работает в этот день ({visit_day_of_week}).')
        
        return data




class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['doctor', 'patient', 'service', 'notes']


class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitRatingSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, default=0)

    def validate_rating(self, value):
        if not (0 <= value <= 5):
            raise serializers.ValidationError('Оценка должна быть от 0 до 5')

        return value

    def validate(self, data):
        if self.instance and self.instance.rating > 0:
            raise serializers.ValidationError('Рейтинг для этого визита уже установлен.')
        return data

    class Meta:
        model = Visit
        fields = ['rating']