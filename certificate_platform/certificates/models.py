from django.db import models
from django.conf import settings
import uuid

class Certificate(models.Model):
    certificate_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='certificates')
    subscription = models.ForeignKey('subscriptions.Subscription', on_delete=models.SET_NULL, null=True)
    candidate = models.ForeignKey('candidates.Candidate', on_delete=models.SET_NULL, null=True, blank=True)
    template = models.ForeignKey('template_manager.CertificateTemplate', on_delete=models.SET_NULL, null=True, blank=True)
    recipient_name = models.CharField(max_length=255)
    recipient_email = models.EmailField()
    course_title = models.CharField(max_length=255)
    issue_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return f"{self.recipient_name} - {self.course_title}"

    class Meta:
        ordering = ['-issue_date']