from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from datetime import date

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # You can create sample data for testing
        self.invoice = Invoice.objects.create(
            customer_name="Test Customer",
            date=date(2022, 1, 1)
        )
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description="Test Description",
            quantity=5,
            unit_price=10
        )

    def test_create_invoice(self):
        data = {
            "customer_name": "New Customer",
            "date": "2022-01-02",
            "details": {
                "description": "New Description",
                "quantity": 3,
                "unit_price": 15
            }
        }
        response = self.client.post('/api/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)
        self.assertEqual(InvoiceDetail.objects.count(), 2)

    def test_get_invoice_list(self):
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_invoice(self):
        response = self.client.get(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        data = {
            "customer_name": "Updated Customer",
            "date": "2022-02-01",
            "details": {
                "description": "Updated Description",
                "quantity": 8,
                "unit_price": 12
            }
        }
        response = self.client.put(f'/api/invoices/{self.invoice.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.invoice.refresh_from_db()
        self.invoice_detail.refresh_from_db()
        self.assertEqual(self.invoice.customer_name, "Updated Customer")
        self.assertEqual(str(self.invoice.date), "2022-02-01")
        self.assertEqual(self.invoice_detail.description, "Updated Description")
        self.assertEqual(self.invoice_detail.quantity, 8)
        self.assertEqual(self.invoice_detail.unit_price, 12)

    def test_delete_invoice(self):
        response = self.client.delete(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)
        self.assertEqual(InvoiceDetail.objects.count(), 0)
