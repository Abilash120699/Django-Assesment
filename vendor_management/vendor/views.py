from django.shortcuts import render
from rest_framework import viewsets
from vendor.serializers import VendorSerializer
from vendor.models import vendor_profile
# Create your views here.



class VendorViewset(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = vendor_profile.objects.all()
    permission_classes = []
    authentication_classes = []