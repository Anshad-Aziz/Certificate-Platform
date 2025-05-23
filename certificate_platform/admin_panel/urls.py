from django.urls import path
from . import views

app_name = 'admin_panel'
urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('companies/', views.company_list_view, name='company_list'),
    path('subscriptions/', views.subscription_list_view, name='subscription_list'),
    path('certificates/', views.certificate_list_view, name='certificate_list'),
]