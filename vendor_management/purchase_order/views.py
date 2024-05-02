from django.shortcuts import render
from django.db.models import Avg,F, ExpressionWrapper, DurationField
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from purchase_order.models import purchase_order, HistoricalPerformance
from django.utils import timezone
from vendor.models import vendor_profile
from purchase_order.serializers import PurchaseSerializer, HistoriacalSerializer


# Create your views here.


def ontime_delivery(vendor):
    completed_po = purchase_order.objects.filter(vendor__id=vendor.id, status='completed')
    on_time_count = completed_po.filter(delivery_date__lte=completed_po.values('order_date')).count()
    total_count = completed_po.count()
    value = (on_time_count/total_count)*100 if total_count > 0 else 0
    return value

def quality_rating_average(vendor):
    po = purchase_order.objects.filter(vendor__id=vendor.id)
    total_ratings = po.aggregate(Avg('quality_rating'))['quality_rating__avg']
    return total_ratings

def calculate_average_response_time(vendor):
    completed_pos = purchase_order.objects.filter(vendor=vendor, status='completed')
    response_times = [po.acknowledgment_date - po.issue_date for po in completed_pos if po.acknowledgment_date]
    average_response_time = sum(rt.total_seconds() for rt in response_times) / len(
        response_times) if response_times else 0
    return average_response_time


def calculate_fulfillment_rate(vendor):
    total_orders = purchase_order.objects.filter(vendor__id=vendor.id).count()
    successful_orders = purchase_order.objects.filter(vendor__id=vendor.id, status='completed').count()
    value = (successful_orders / total_orders) * 100 if total_orders > 0 else 0
    return value



class PurchaseViewset(viewsets.ModelViewSet):
    queryset = purchase_order.objects.all()
    serializer_class = PurchaseSerializer

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        po = purchase_order.objects.get(id=pk)
        if po.acknowledgment_date is None:
            po.acknowledgment_date = timezone.now()
            po.save()
        return Response({'status': 'acknowledged'})

class HistoricalViewset(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoriacalSerializer