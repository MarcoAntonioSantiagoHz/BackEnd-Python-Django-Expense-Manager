"""
URL configuration for expenses_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from core_api.views.account_views import create_account, delete_account, get_account_by_id, get_accounts, update_account
from core_api.views.expense_views import create_expense, get_expense_by_id, get_expenses, patch_expense_status, update_expense
from core_api.views.payment_views import create_payment, get_payment_by_id, get_payments, patch_payment_status, update_payment

urlpatterns = [
    path('admin/', admin.site.urls),
    # all registers urls of project 
    # Paths route accounts
    # path('api/v1/accounts/create/', create_account, name='create_account'), 
    # path('api/v1/accounts/', get_accounts, name='get_accounts'),
    # path('api/v1/accounts/update/<int:account_id>/', update_account),
    # path('api/v1/accounts/delete/<int:account_id>/', delete_account),
    # path('api/v1/accounts/<int:account_id>/', get_account_by_id),

    path('api/v1/accounts/', get_accounts, name='get_accounts'),                # GET
    path('api/v1/accounts/create', create_account, name='create_account'),            # POST
    path('api/v1/accounts/<int:account_id>/', get_account_by_id),              # GET (uno)
    path('api/v1/accounts/update/<int:account_id>/', update_account),                 # PUT/PATCH
    path('api/v1/accounts/delete/<int:account_id>/', delete_account),                 # DELETE


    # Paths route expenses
    path('api/v1/expenses/create/', create_expense, name='create_expense'),
    # path('api/v1/expenses/', create_expense, name='create_expense'),
    path('api/v1/expenses/', get_expenses),
    path('api/v1/expenses/update/<int:expense_id>/', update_expense),                 # PUT/PATCH
    path('api/v1/expenses/<int:expense_id>/', get_expense_by_id),
    path('api/v1/expenses/<int:expense_id>/status/', patch_expense_status, name='patch_expense_status'),

    # Paths route payments
    path('api/v1/payments/create/', create_payment, name='create_payment'),
    path('api/v1/payments/', get_payments),
    path('api/v1/payments/update/<int:payment_id>/', update_payment),                 # PUT/PATCH
    path('api/v1/payments/<int:payment_id>/', get_payment_by_id),
    path('api/v1/payments/<int:payment_id>/status/', patch_payment_status, name='patch_payment_status'),



]
