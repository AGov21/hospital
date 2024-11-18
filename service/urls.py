from django.urls import path
from service.views import ServiceView


app_name = 'service'

urlpatterns = [
    path('', ServiceView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', ServiceView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),



]