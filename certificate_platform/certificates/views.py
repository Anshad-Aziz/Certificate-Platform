from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Certificate
from subscriptions.models import Subscription
from candidates.models import Candidate
from template_manager.models import CertificateTemplate
from .qr_code_generator import generate_qr_code
from weasyprint import HTML
from django.template.loader import render_to_string
from django.conf import settings

@login_required
def certificate_generate_view(request):
    subscription = Subscription.objects.filter(company=request.user, is_active=True).first()
    if not subscription:
        messages.error(request, 'You need an active subscription to generate certificates.')
        return redirect('subscriptions:plan_list')
    if subscription.certificates_used >= subscription.plan.certificate_quota:
        messages.error(request, 'Certificate quota reached for this month.')
        return redirect('subscriptions:details')
    
    candidates = Candidate.objects.filter(company=request.user)
    templates = CertificateTemplate.objects.filter(company=request.user)
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        template_id = request.POST.get('template_id')
        course_title = request.POST.get('course_title')
        try:
            candidate = Candidate.objects.get(id=candidate_id, company=request.user)
            template = CertificateTemplate.objects.get(id=template_id, company=request.user) if template_id else None
            certificate = Certificate.objects.create(
                company=request.user,
                subscription=subscription,
                candidate=candidate,
                template=template,
                recipient_name=f"{candidate.first_name} {candidate.last_name}",
                recipient_email=candidate.email,
                course_title=course_title
            )
            generate_qr_code(certificate)
            subscription.certificates_used += 1
            subscription.save()
            messages.success(request, f'Certificate generated for {candidate.first_name} {candidate.last_name}!')
            return redirect('certificates:list')
        except (Candidate.DoesNotExist, CertificateTemplate.DoesNotExist):
            messages.error(request, 'Selected candidate or template not found.')
    
    return render(request, 'certificates/generate.html', {'subscription': subscription, 'candidates': candidates, 'templates': templates})

@login_required
def certificate_download_view(request, certificate_id):
    certificate = get_object_or_404(Certificate, certificate_id=certificate_id, company=request.user)
    
    # Render certificate HTML
    html_content = render_to_string('certificates/certificate_pdf.html', {
        'certificate': certificate,
        'qr_code_url': certificate.qr_code.url if certificate.qr_code else '',
        'SITE_URL': settings.SITE_URL,
    })
    
    # Generate PDF with WeasyPrint
    html = HTML(string=html_content, base_url=settings.SITE_URL)
    pdf_file = html.write_pdf()
    
    # Create response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{certificate.certificate_id}.pdf"'
    response.write(pdf_file)
    
    return response

@login_required
def certificate_list_view(request):
    certificates = Certificate.objects.filter(company=request.user).order_by('-issue_date')
    return render(request, 'certificates/list.html', {'certificates': certificates})