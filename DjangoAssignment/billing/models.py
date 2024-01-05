from django.db import models
import datetime
class Invoice(models.Model):
    date = models.DateField(db_index=True,default=datetime.date.today, null=True, blank=True)
    customer_name = models.CharField(db_index=True,max_length=255)

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer_name}"

class InvoiceDetail(models.Model):
    invoice = models.OneToOneField(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detail #{self.id} - {self.description}"

