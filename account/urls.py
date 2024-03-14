from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    
    path("", views.startPage, name="index"),
    path("transaction_page/", views.transactionPage, name="transact"),
    path("create_account/", views.createAccount, name="createAccount"),
    path('transaction/', views.transaction, name='transaction'),
    path("get_balance/<int:account_id>/<str:amount>", views.getBalance, name="getBalance"),
    path("withdraw/<int:account_id>/<str:amount>", views.withdraw, name="withdraw"),
    path("deposit/<int:account_id>/<str:amount>", views.deposit, name="deposit"),
    
]
