from django.shortcuts import render,get_object_or_404
from django.conf import settings
from django.contrib import messages
from certificates.models import Certificate


def verify_certificate_view(request):
    if request.method == 'POST':
        certificate_id = request.POST.get('certificate_id')
        try:
            certificate = Certificate.objects.get(certificate_id=certificate_id)
            messages.success(request, 'Certificate verified successfully.')
            return render(request, 'verification/result.html', {'certificate': certificate, 'SITE_URL': settings.SITE_URL})
        except Certificate.DoesNotExist:
            messages.error(request, 'Invalid Certificate ID.')
            return render(request, 'verification/result.html', {'certificate': None})
    return render(request, 'verification/verify.html')