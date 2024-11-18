from django.contrib import admin
from visit.models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'service', 'status', 'visit_date_time', 'end_date_time']


admin.site.register(Visit, VisitAdmin)