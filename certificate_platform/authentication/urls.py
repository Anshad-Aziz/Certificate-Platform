from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    path('profile/', views.profile_view, name='profile'),
    path('company_profile/', views.company_profile_view, name='company_profile'),
]