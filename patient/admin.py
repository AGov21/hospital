from django.contrib import admin
from patient.models import Patient, MedicalHistory

class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'age', 'user']


admin.site.register(Patient, PatientAdmin)
admin.site.register(MedicalHistory)


