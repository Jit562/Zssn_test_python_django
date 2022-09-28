from django.urls import path
from .views import *

urlpatterns = [
    path('location/', LocationList.as_view(), name='location-list'),
    path('location/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('survivor/', SurvivorList.as_view(), name='survivor-list'),
    path('survivor/<int:pk>/', SurvivorDetail.as_view(), name='survivor-detail'),
]