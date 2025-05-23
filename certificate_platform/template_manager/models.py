from django.db import models
from django.conf import settings

class CertificateTemplate(models.Model):
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='certificate_templates')
    name = models.CharField(max_length=100, help_text="Name of the template (e.g., 'Standard Certificate')")
    html_content = models.TextField(help_text="HTML content for the certificate layout")
    css_content = models.TextField(blank=True, help_text="CSS styles for the certificate")
    is_default = models.BooleanField(default=False, help_text="Set as default template for the company")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.company.company_name})"

    class Meta:
        ordering = ['name']
        unique_together = ['company', 'name']

    def save(self, *args, **kwargs):
        # Ensure only one template is default per company
        if self.is_default:
            CertificateTemplate.objects.filter(company=self.company, is_default=True).exclude(id=self.id).update(is_default=False)
        super().save(*args, **kwargs)