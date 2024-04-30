from django.db import models
from vendor.models import vendor_profile
# Create your models here.



class purchase_order(models.Model):
    po_number = models.CharField(max_length=255)
    vendor = models.ForeignKey(vendor_profile, on_delete=models.CASCADE, null=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(vendor_profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()