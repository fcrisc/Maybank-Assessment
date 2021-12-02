from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', views.apiOverview, name="api-overview"),
]