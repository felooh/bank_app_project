from django.contrib import admin
from .models import Account,Withdraw,Deposit

# Register your models here.
admin.site.register((Account,Withdraw,Deposit))