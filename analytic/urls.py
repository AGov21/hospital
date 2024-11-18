from django.urls import path
from analytic.views import AnalyticsView

app_name = 'analytic'

urlpatterns = [
    path('', AnalyticsView.as_view({
        'get': 'get_analytics'
    }))
]