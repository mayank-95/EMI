from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Accounts
from django.template import loader
from .models import Payments


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def view_accounts(request):
    accounts_list = Accounts.objects.order_by('id')[:]
    context = {'accounts_list': accounts_list}
    return render(request, 'accounts.html', context)

def view_collections(request, account_id):
    return HttpResponse("view collections.")

def view_payments(request):
    payments_list = Payments.objects.order_by('id')[:]
    context = {'payments_list': payments_list}
    return render(request, 'payments.html', context)