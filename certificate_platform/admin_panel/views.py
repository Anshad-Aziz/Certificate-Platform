from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authentication.models import CustomUser
from subscriptions.models import Subscription
from certificates.models import Certificate
from django.contrib.auth import get_user_model

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            messages.error(request, 'You do not have permission to access the admin panel.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
@admin_required
def dashboard_view(request):
    total_companies = CustomUser.objects.count()
    total_subscriptions = Subscription.objects.filter(is_active=True).count()
    total_certificates = Certificate.objects.count()
    context = {
        'total_companies': total_companies,
        'total_subscriptions': total_subscriptions,
        'total_certificates': total_certificates,
    }
    return render(request, 'admin_panel/dashboard.html', context)

@login_required
@admin_required
def company_list_view(request):
    companies = CustomUser.objects.all()
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        action = request.POST.get('action')
        try:
            company = CustomUser.objects.get(id=company_id)
            if action == 'activate':
                company.is_active = True
                company.save()
                messages.success(request, f'Company {company.company_name} activated.')
            elif action == 'deactivate':
                company.is_active = False
                company.save()
                messages.success(request, f'Company {company.company_name} deactivated.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Company not found.')
        return redirect('admin_panel:company_list')
    return render(request, 'admin_panel/company_list.html', {'companies': companies})

@login_required
@admin_required
def subscription_list_view(request):
    subscriptions = Subscription.objects.select_related('company', 'plan').all()
    return render(request, 'admin_panel/subscription_list.html', {'subscriptions': subscriptions})

@login_required
@admin_required
def certificate_list_view(request):
    certificates = Certificate.objects.select_related('company', 'subscription').all()
    return render(request, 'admin_panel/certificate_list.html', {'certificates': certificates})