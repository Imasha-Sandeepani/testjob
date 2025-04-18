from django.urls import path
from . import views
from .views import logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/complete/', views.profile_complete, name='profile_complete'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('post-job/', views.post_job, name='post_job'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='jobs/login.html'), name='login'),

]