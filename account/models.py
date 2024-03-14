from django.db import models

# Create your models here.

class Account(models.Model):
    customer_id = models.IntegerField()
    account_id = models.IntegerField()
    balance = models.IntegerField(default="0")

    def __str__(self):
        return f"Account: {self.account_id}"

class Withdraw(models.Model):
    account = models.ForeignKey(Account, related_name='withdrawals', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Withdraw: {self.amount}"


class Deposit(models.Model):
    account = models.ForeignKey(Account, related_name='deposits', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Deposit: {self.amount}"
