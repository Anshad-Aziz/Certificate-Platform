from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CertificateTemplate
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
from django.conf import settings

@login_required
def template_list_view(request):
    templates = CertificateTemplate.objects.filter(company=request.user).order_by('name')
    return render(request, 'template_manager/list.html', {'templates': templates})

@login_required
def template_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        html_content = request.POST.get('html_content')
        css_content = request.POST.get('css_content')
        is_default = request.POST.get('is_default') == 'on'
        try:
            template = CertificateTemplate.objects.create(
                company=request.user,
                name=name,
                html_content=html_content,
                css_content=css_content,
                is_default=is_default
            )
            messages.success(request, f'Template "{name}" created successfully!')
            return redirect('template_manager:list')
        except Exception as e:
            messages.error(request, f'Error creating template: {str(e)}')
    return render(request, 'template_manager/create.html')

@login_required
def template_edit_view(request, template_id):
    template = get_object_or_404(CertificateTemplate, id=template_id, company=request.user)
    if request.method == 'POST':
        template.name = request.POST.get('name')
        template.html_content = request.POST.get('html_content')
        template.css_content = request.POST.get('css_content')
        template.is_default = request.POST.get('is_default') == 'on'
        try:
            template.save()
            messages.success(request, f'Template "{template.name}" updated successfully!')
            return redirect('template_manager:list')
        except Exception as e:
            messages.error(request, f'Error updating template: {str(e)}')
    return render(request, 'template_manager/edit.html', {'template': template})

@login_required
def template_preview_view(request, template_id):
    template = get_object_or_404(CertificateTemplate, id=template_id, company=request.user)
    
    # Mock certificate data for preview
    mock_certificate = {
        'recipient_name': 'John Doe',
        'course_title': 'Sample Course',
        'company': {'company_name': request.user.company_name},
        'issue_date': '2025-05-07',
        'certificate_id': '123e4567-e89b-12d3-a456-426614174000',
    }
    
    # Render preview HTML
    html_content = render_to_string('template_manager/preview.html', {
        'certificate': mock_certificate,
        'template': template,
        'SITE_URL': settings.SITE_URL,
    })
    
    # Generate PDF with WeasyPrint
    html = HTML(string=html_content, base_url=settings.SITE_URL)
    pdf_file = html.write_pdf()
    
    # Return PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="template_preview_{template.id}.pdf"'
    response.write(pdf_file)
    
    return response