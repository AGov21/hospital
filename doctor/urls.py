from django.urls import path
from doctor.views.doctor import DoctorView
from doctor.views.schedule import ScheduleView

app_name = 'doctor'

urlpatterns = [
    path('', DoctorView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', DoctorView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('<int:pk>/patient/', DoctorView.as_view({
        'get': 'list_patient',
    })),

    path('schedule/', ScheduleView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('schedule/<int:pk>/', ScheduleView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

]