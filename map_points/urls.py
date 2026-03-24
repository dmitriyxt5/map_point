from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_point, name='add_point'),
    path('success/', views.point_success, name='point_success'),
]
