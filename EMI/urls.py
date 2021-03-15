from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.view_accounts, name='account'),
    path('<int:account_id>/collections/', views.view_collections, name='collections'),
    path('payments/', views.view_payments, name='payments'),
]