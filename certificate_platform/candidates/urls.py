from django.urls import path
from . import views

app_name = 'candidates'
urlpatterns = [
    path('', views.candidate_list_view, name='list'),
    path('create/', views.candidate_create_view, name='create'),
    path('edit/<int:candidate_id>/', views.candidate_edit_view, name='edit'),
    path('delete/<int:candidate_id>/', views.candidate_delete_view, name='delete'),
    path('upload/', views.candidate_upload_view, name='upload'),
]