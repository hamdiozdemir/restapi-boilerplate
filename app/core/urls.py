"""
URL mappings for core app.
"""
from django.urls import path, include
from .views import BasicAPIView

app_name = 'core'


urlpatterns = [
    path('', BasicAPIView.as_view(), name='index'),
]
