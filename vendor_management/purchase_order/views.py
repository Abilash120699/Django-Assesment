from django.shortcuts import render
from rest_framework import viewsets
from purchase_order.models import purchase_order
from purchase_order.serializers import PurchaseSerializer
# Create your views here.




class PurchaseViewset(viewsets.ModelViewSet):
    queryset = purchase_order.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = []
    authentication_classes = []