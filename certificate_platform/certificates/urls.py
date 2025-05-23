from django.urls import path
from . import views

app_name = 'certificates'
urlpatterns = [
    path('', views.certificate_list_view, name='list'),
    path('generate/', views.certificate_generate_view, name='generate'),
    path('download/<uuid:certificate_id>/', views.certificate_download_view, name='download'),
]