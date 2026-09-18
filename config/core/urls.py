from django.urls import path
from .views import health_check, eventos

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('eventos/', eventos, name='eventos'),
]