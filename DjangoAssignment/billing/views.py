from rest_framework import generics
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all().prefetch_related('details__invoice')
    serializer_class = InvoiceSerializer


class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer