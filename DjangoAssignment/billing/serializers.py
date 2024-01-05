from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ["description","quantity","unit_price","price"]

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(required=False)

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details', None)
        invoice = Invoice.objects.create(**validated_data)

        if details_data:
            InvoiceDetail.objects.create(invoice=invoice, **details_data)

        return invoice
    
    def update(self, instance, validated_data):

        # Update Invoice fields
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()

        # Update associated InvoiceDetail instances
        details_data = validated_data.get('details', None)
        if details_data:
            detail = instance.details
            if detail:
                detail.description = details_data.get('description', detail.description)
                detail.quantity = details_data.get('quantity', detail.quantity)
                detail.unit_price = details_data.get('unit_price', detail.unit_price)
                detail.save()

        return instance