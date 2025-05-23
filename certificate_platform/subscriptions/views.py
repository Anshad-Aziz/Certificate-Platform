from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Plan, Subscription

stripe.api_key = settings.STRIPE_SECRET_KEY
def plan_list_view(request):
    plans = Plan.objects.all()
    return render(request, 'subscriptions/plans.html', {'plans': plans})

@login_required
def subscribe_view(request, plan_id):
    plan = Plan.objects.get(id=plan_id, is_active=True)
    if request.method == 'POST':
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': plan.stripe_price_id,
                    'quantity': 1,
                }],
                mode='subscription',
                success_url='http://127.0.0.1:8000/subscriptions/success/?session_id={CHECKOUT_SESSION_ID}',
                cancel_url='http://127.0.0.1:8000/subscriptions/cancel/',
                client_reference_id=str(request.user.id),
            )
            return redirect(session.url, code=303)
        except Exception as e:
            messages.error(request, f'Error creating checkout session: {str(e)}')
            return redirect('subscriptions:subscribe', plan_id=plan_id)
    return render(request, 'subscriptions/subscribe.html', {'plan': plan})

@login_required
def success_view(request):
    session_id = request.GET.get('session_id')
    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            if session.payment_status == 'paid':
                messages.success(request, 'Subscription created successfully!')
            else:
                messages.error(request, 'Payment not completed.')
        except Exception as e:
            messages.error(request, f'Error verifying payment: {str(e)}')
    return render(request, 'subscriptions/success.html')

@login_required
def cancel_view(request):
    messages.error(request, 'Subscription cancelled.')
    return render(request, 'subscriptions/cancel.html')

@csrf_exempt
def webhook_view(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        if session['payment_status'] == 'paid':
            client_reference_id = session.get('client_reference_id')
            subscription_id = session['subscription']
            plan = Plan.objects.get(stripe_price_id=session['line_items']['data'][0]['price']['id'])
            if client_reference_id.startswith('pending_user:'):
                _, username, email, password = client_reference_id.split(':')
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                Subscription.objects.create(
                    company=user,
                    plan=plan,
                    stripe_subscription_id=subscription_id,
                    start_date=timezone.now().date(),
                    is_active=True
                )
            else:
                user_id = client_reference_id
                user = User.objects.get(id=user_id)
                Subscription.objects.create(
                    company=user,
                    plan=plan,
                    stripe_subscription_id=subscription_id,
                    start_date=timezone.now().date(),
                    is_active=True
                )

    return HttpResponse(status=200)

@login_required
def subscription_details_view(request):
    subscription = Subscription.objects.filter(company=request.user, is_active=True).first()
    if not subscription:
        messages.info(request, 'No active subscription found.')
    return render(request, 'subscriptions/details.html', {'subscription': subscription})