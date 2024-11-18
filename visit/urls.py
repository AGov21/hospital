from django.urls import path
from visit.views import VisitView

app_name = 'visit'

urlpatterns = [

    path('', VisitView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', VisitView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

    path('<int:pk>/rating', VisitView.as_view({
        'put': 'set_rating'
    })),


]