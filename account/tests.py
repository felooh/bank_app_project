from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Account

class APITests(TestCase):

    def setUp(self):
        self.client = Client()
        # Create a test account for use in the tests
        self.account = Account.objects.create(customer_id=1, account_id=1, balance=10000)

    def test_get_balance(self):
        # Test getBalance API
        response = self.client.get(
            f'/get_balance/{self.account.account_id}/{1000}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.account.balance)

    def test_withdraw(self):
        # Test withdraw API
        withdraw_amount = 5000
        response = self.client.post(
            f'/withdraw/{self.account.account_id}/{withdraw_amount}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Withdrawal request received")

        # Check if balance has been updated correctly
        updated_account = Account.objects.get(account_id=self.account.account_id)
        self.assertEqual(updated_account.balance, self.account.balance - withdraw_amount)

    def test_deposit(self):
        # Test deposit API
        deposit_amount = 2000
        response = self.client.post(
            f'/deposit/{self.account.account_id}/{deposit_amount}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Deposit request received")

        # Check if balance has been updated correctly
        updated_account = Account.objects.get(account_id=self.account.account_id)
        self.assertEqual(updated_account.balance, self.account.balance + deposit_amount)
