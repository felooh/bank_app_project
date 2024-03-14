from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from .models import Account, Withdraw, Deposit
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
import datetime
from django.contrib import messages
from django.http import HttpResponse



# Create your views here.
#index
def startPage(request):
    
    return render(request, 'pages/index.html')

def transactionPage(request):
    return render(request, 'pages/transactionPage.html')

    

# createAccount
def createAccount(request):
    latest_account = Account.objects.order_by('-customer_id').first()
    if latest_account:
        next_customer_id = latest_account.id + 1
    else:
        next_customer_id = 1

    balance = 0
    account = Account.objects.create(customer_id=next_customer_id, account_id=next_customer_id, balance=balance)
    account.save()
    context ={
        "customer_id": next_customer_id,
        "account_id": next_customer_id,
        "balance": balance,
        "account": account
    }
    return render(request, 'pages/transactionPage.html', context)

    
#transaction
def transaction(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        amount = request.POST.get('amount')
        account_id = request.POST.get('account_id')
        
        
        print(account_id)
        print(amount)

        if action == 'deposit':
            deposit(request, account_id, amount)
        elif action == 'withdraw':
            withdraw(request, account_id, amount)
                
        account = Account.objects.filter(account_id=account_id).first()
        
        messages.get_messages(request)

        context ={
            "action": action,
            "amount": amount,
            "account_id": account_id,
            "customer_id": account.customer_id,
            "balance": account.balance,     
        }

    return render(request, 'pages/transactionPage.html', context)

#get_balance API 
def getBalance(request, account_id, amount):
    account = Account.objects.filter(account_id=account_id).first()
    
    if account:
        context ={
            "balance": account.balance,
        }
        messages.success(request, f"Your current balance is {{account.balance}} successful.")
        return render(request, 'pages/transactionPage.html', context)
    else:
        messages.error(request, "Account does not exist")
        return render(request, 'pages/transactionPage.html')
    
#withdraw API
def withdraw(request, account_id, amount):
    account = Account.objects.filter(account_id=account_id).first()
    withdrawals = Withdraw.objects.filter(account=account, date=timezone.now().date())
    
    if withdrawals.count() >= 3:
        messages.warning(request, "Exceeded Maximum number of withdrawals(3) per day")
        return render(request, 'pages/transactionPage.html')
        
    
    if account is None and amount is None:
        messages.error(request, "Invalid withdrawal amount. Kindly enter a figure.")
        return render(request, 'pages/transactionPage.html')
    
    if float(amount) > 20000:      
        messages.warning(request, "Exceeded Maximum Withdrawal Per Transaction")
        return render(request, 'pages/transactionPage.html')
    
    if account.balance < float(amount):
        messages.error(request, "Insufficient Balance")
        return HttpResponse(status=404)

        # return render(request, 'pages/index.html')
    
    today_withdrawals = Withdraw.objects.filter(account=account, date=timezone.now().date()).values_list('amount', flat=True)

    total_withdrawals= sum(today_withdrawals)
    
    if total_withdrawals + float(amount) > 50000:
        messages.warning(request, "Exceeded Maximum Withdrawal for the day")
        return render(request, 'pages/transactionPage.html')
    
    withdraw = Withdraw.objects.create(account=account, amount=amount)
    account.balance -= float(amount)
    account.save()
    withdraw.save()
    
    messages.success(request, "Withdrawal request received. Processing...")
    return render(request, 'pages/transactionPage.html')

#Deposit API
def deposit(request, account_id, amount):
    account = Account.objects.filter(account_id=account_id).first()
    deposit = Deposit.objects.filter(account=account, date=timezone.now().date())
    
    if deposit.count() >= 4:
        messages.warning(request, "Exceeded Maximum number of deposit(4 deposits) per day")
        return render(request, 'pages/transactionPage.html')
        
    if account is None and amount is None:
        messages.error(request, "Invalid deposit amount")        
        return render(request, 'pages/transactionPage.html')
    
    if int(amount) > 40000:
        messages.warning(request, "Exceeded Maximum Deposit(KES 40K) Per Transaction.")
        return render(request, 'pages/transactionPage.html')
    
   
    today_deposit = Deposit.objects.filter(account=account, date=timezone.now().date()).values_list('amount', flat=True)

    total_deposit= sum(today_deposit)
    
    if total_deposit + int(amount) > 150000:
        
        messages.warning(request, "Exceeded Maximum deposit(KES 150K) for the day.")
        return render(request, 'pages/transactionPage.html')
    
    deposit = Deposit.objects.create(account=account, amount=amount)
    account.balance += int(amount)
    account.save()
    deposit.save()
    
    context ={
        "customer_id": account_id,
        "account_id": account_id,
        "account": account
    }
    messages.success(request, "Deposit request received. Processing...")
    return render(request, 'pages/transactionPage.html', context)




    

        
    
    
    
        
