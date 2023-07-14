from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.InvoiceListAPIView.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', views.InvoiceDetailAPIView.as_view(), name='invoice-detail'),
]
