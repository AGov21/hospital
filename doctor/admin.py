from django.contrib import admin
from doctor.models import Doctor, Schedule

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'specialization', 'department']


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'day_of_week', 'start_time', 'end_time']



admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Schedule, ScheduleAdmin)

