from django.urls import path
from . import views

app_name = 'verification'
urlpatterns = [
    path('', views.verify_certificate_view, name='verify'),
    path('<uuid:certificate_id>/', views.verify_certificate_view, name='verify_by_id'),
]