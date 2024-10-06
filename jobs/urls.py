
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('post-job/', views.post_job, name='post_job'),
    path('signup/', views.signup, name='signup'),  # Sign up page
]

