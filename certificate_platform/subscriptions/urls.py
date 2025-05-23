from django.urls import path
from . import views

app_name = 'subscriptions'
urlpatterns = [
    path('plans/', views.plan_list_view, name='plan_list'),
    path('subscribe/<int:plan_id>/', views.subscribe_view, name='subscribe'),
    path('details/', views.subscription_details_view, name='details'),    path('success/', views.success_view, name='success'),
    path('cancel/', views.cancel_view, name='cancel'),
    path('webhook/', views.webhook_view, name='webhook'),
]

