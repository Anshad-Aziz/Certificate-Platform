from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('authentication/', include('authentication.urls')),
    path('subscriptions/', include('subscriptions.urls')),
    path('templates/', include('template_manager.urls')),
    path('candidates/', include('candidates.urls')),
    path('certificates/', include('certificates.urls')),
    path('verification/', include('verification.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin-panel/', include('admin_panel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)