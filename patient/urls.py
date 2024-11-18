from django.urls import path
from patient.views import PatientView, MedicalHistoryView


app_name = 'patient'

urlpatterns = [
    path('', PatientView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', PatientView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

    path('medical-history/', MedicalHistoryView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('medical-history/<int:pk>/', MedicalHistoryView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

]