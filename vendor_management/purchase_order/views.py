from django.shortcuts import render
from django.db.models import Avg
from rest_framework import viewsets
from purchase_order.models import purchase_order
from vendor.models import vendor_profile
from purchase_order.serializers import PurchaseSerializer
# Create your views here.


def ontime_delivery(vendor):
    completed_po = purchase_order.objects.filter(vendor__id=vendor.id, status='completed')
    on_time_count = completed_po.filter(delivery_date__lte=completed_po.values('order_date')).count()
    total_count = completed_po.count()
    value = (on_time_count/total_count)*100
    return value

def quality_rating_average(vendor):
    po = purchase_order.objects.filter(vendor__id=vendor.id)
    total_ratings = po.aggregate(Avg('quality_rating'))['quality_rating__avg']
    return total_ratings

def calculate_average_response_time(vendor):
    acknowledged_orders = purchase_order.objects.filter(vendor__id=vendor.id, acknowledgment_date__isnull=False)
    total_response_time = acknowledged_orders.aggregate(
        Avg('acknowledgment_date') - Avg('issue_date')
    )
    value = total_response_time['acknowledgment_date__avg'] / 3600
    return value


def calculate_fulfillment_rate(vendor):
    total_orders = purchase_order.objects.filter(vendor__id=vendor.id).count()
    successful_orders = purchase_order.objects.filter(vendor__id=vendor.id, status='completed').count()
    value = (successful_orders / total_orders) * 100
    return value



class PurchaseViewset(viewsets.ModelViewSet):
    queryset = purchase_order.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = []
    authentication_classes = []