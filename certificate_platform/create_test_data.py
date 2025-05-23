from django.test import TestCase, Client
from django.contrib.auth.models import User
from subscriptions.models import Plan, Subscription
from django.urls import reverse

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.plan = Plan.objects.create(
            name="Basic Plan", price=10.00, certificate_quota=50, stripe_price_id="price_1Test123"
        )

    def test_register_post_valid(self):
        response = self.client.post(reverse('authentication:register'), {
            'username': 'newuser',
            'email': 'newuser@company.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'plan_id': self.plan.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect to Stripe