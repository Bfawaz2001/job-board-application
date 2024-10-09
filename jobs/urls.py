from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  # Ensure this exists
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('post-job/', views.post_job, name='post_job'),
    path('my-job-postings/', views.my_job_postings, name='my_job_postings'),
    path('edit-job/<int:pk>/', views.edit_job, name='edit_job'),
    path('delete-job/<int:pk>/', views.delete_job, name='delete_job'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('', views.job_list, name='job_list'),
    path('application/<int:pk>/update-status/', views.update_application_status, name='update_application_status'),
    path('application-history/', views.application_history, name='application_history'),
]
