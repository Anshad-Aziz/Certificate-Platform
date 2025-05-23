from django.contrib import admin
from .models import CertificateTemplate

@admin.register(CertificateTemplate)
class CertificateTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'is_default', 'created_at']
    search_fields = ['name', 'company__company_name']
    list_filter = ['company', 'is_default']