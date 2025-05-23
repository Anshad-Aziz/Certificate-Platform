from django import forms
from candidates.models import Candidate
from certificates.models import Certificate
from template_manager.models import Template

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['candidate', 'template', 'dynamic_data']

    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        if company:
            self.fields['candidate'].queryset = Candidate.objects.filter(company=company)
            self.fields['template'].queryset = Template.objects.filter(company=company)