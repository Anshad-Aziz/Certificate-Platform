from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_id', 'recipient_name', 'course_title', 'company', 'issue_date', 'is_valid']
    search_fields = ['recipient_name', 'course_title', 'certificate_id']
    list_filter = ['is_valid', 'company']