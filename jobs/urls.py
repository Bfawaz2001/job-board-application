from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),  # Job detail route
]

