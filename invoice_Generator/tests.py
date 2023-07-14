from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice1 = Invoice.objects.create(date='2022-01-01', invoice_no='INV-001', customer_name='John Doe')
        self.invoice2 = Invoice.objects.create(date='2022-02-01', invoice_no='INV-002', customer_name='Jane Smith')

        self.invoice_detail1 = InvoiceDetail.objects.create(
            invoice=self.invoice1,
            description='Item 1',
            quantity=2,
            unit_price=10.0,
            price=20.0
        )
        self.invoice_detail2 = InvoiceDetail.objects.create(
            invoice=self.invoice2,
            description='Item 2',
            quantity=3,
            unit_price=15.0,
            price=45.0
        )

    def test_get_invoices(self):
        url = reverse('invoice-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice1.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['invoice_no'], 'INV-001')
        self.assertEqual(len(response.data['invoice_details']), 1)

    def test_create_invoice(self):
        url = reverse('invoice-list')
        data = {
            'date': '2022-03-01',
            'invoice_no': 'INV-003',
            'customer_name': 'Alice Brown',
            'invoice_details': [
                {
                    'description': 'Item 3',
                    'quantity': 1,
                    'unit_price': 5.0,
                    'price': 5.0
                }
            ]
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['invoice_no'], 'INV-003')
        self.assertEqual(len(response.data['invoice_details']), 1)

    def test_update_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice2.pk})
        data = {
            'date': '2022-02-15',
            'invoice_no': 'INV-002-updated',
            'customer_name': 'Jane Smith (Updated)',
            'invoice_details': [
                {
                    'description': 'Item 2 (Updated)',
                    'quantity': 4,
                    'unit_price': 15.0,
                    'price': 60.0
                }
            ]
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['invoice_no'], 'INV-002-updated')
        self.assertEqual(response.data['customer_name'], 'Jane Smith (Updated)')
        self.assertEqual(len(response.data['invoice_details']), 1)

    def test_delete_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice1.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Invoice.objects.filter(pk=self.invoice1.pk).exists())
        self.assertFalse(InvoiceDetail.objects.filter(invoice=self.invoice1).exists())
