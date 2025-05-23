from django import forms

class CertificateVerificationForm(forms.Form):
    certificate_id = forms.CharField(max_length=100, label='Certificate ID')