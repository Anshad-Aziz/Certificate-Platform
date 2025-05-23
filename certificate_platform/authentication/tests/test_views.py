from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from subscriptions.models import Plan
from unittest.mock import patch

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.plan = Plan.objects.create(
            name="Basic Plan",
            price=10.00,
            certificate_quota=50,
            stripe_price_id="price_1Xyz123"  # Replace with your actual Basic Plan Price ID
        )
        self.register_url = reverse('authentication:register')

    @patch('stripe.checkout.Session.create')
    def test_register_post_valid(self, mock_stripe_create):
        mock_stripe_create.return_value = {
            'id': 'cs_test_123',
            'url': 'https://checkout.stripe.com/pay/cs_test_123'
        }
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@company.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'plan_id': self.plan.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('https://checkout.stripe.com'))
        mock_stripe_create.assert_called_once()
        call_args = mock_stripe_create.call_args[1]
        self.assertTrue(call_args['client_reference_id'].startswith('pending_user:newuser:newuser@company.com:'))

    def test_register_post_invalid_form(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@company.com',
            'password1': 'testpass123',
            'password2': 'differentpass',
            'plan_id': self.plan.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please correct the form errors.')

    def test_register_post_invalid_plan(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@company.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'plan_id': 999
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Selected plan is invalid.')