from django.urls import path
from . import views

app_name = 'template_manager'
urlpatterns = [
    path('', views.template_list_view, name='list'),
    path('create/', views.template_create_view, name='create'),
    path('edit/<int:template_id>/', views.template_edit_view, name='edit'),
    path('preview/<int:template_id>/', views.template_preview_view, name='preview'),
]