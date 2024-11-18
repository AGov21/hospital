from django.urls import path
from specialization.views import SpecializationView


app_name = 'specialization'

urlpatterns = [

    path('', SpecializationView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', SpecializationView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),



]