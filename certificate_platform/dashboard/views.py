from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from certificates.models import Certificate
from subscriptions.models import Subscription
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import datetime
from django.contrib import messages
from candidates.models import Candidate
import json
@login_required
def dashboard_view(request):
    subscription = Subscription.objects.filter(company=request.user, is_active=True).first()
    candidate_count = Candidate.objects.filter(company=request.user).count()
    certificate_count = Certificate.objects.filter(company=request.user).count()

    # Certificate issuance by month
    certificate_data = (
        Certificate.objects.filter(company=request.user)
        .annotate(month=TruncMonth('issue_date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    certificate_months = [entry['month'].strftime('%Y-%m') for entry in certificate_data]
    certificate_counts = [entry['count'] for entry in certificate_data]

    # Candidate registration by month
    candidate_data = (
        Candidate.objects.filter(company=request.user)
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    candidate_months = [entry['month'].strftime('%Y-%m') for entry in candidate_data]
    candidate_counts = [entry['count'] for entry in candidate_data]

    if not subscription:
        messages.info(request, 'No active subscription found. Please subscribe to a plan.')

    context = {
        'subscription': subscription,
        'candidate_count': candidate_count,
        'certificate_count': certificate_count,
        'certificate_months': json.dumps(certificate_months),
        'certificate_counts': json.dumps(certificate_counts),
        'candidate_months': json.dumps(candidate_months),
        'candidate_counts': json.dumps(candidate_counts),
    }
    return render(request, 'dashboard/dashboard.html', context)