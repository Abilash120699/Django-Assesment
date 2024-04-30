from django.shortcuts import render
from rest_framework import viewsets, status
from vendor.serializers import VendorSerializer, VendorListSerializer, VendorPerformanceSerializer
from vendor.models import vendor_profile
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.



class VendorViewset(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = vendor_profile.objects.all()
    permission_classes = []
    authentication_classes = []

    def get_serializer_class(self):
        if self.action == 'list':
            return VendorListSerializer
        if self.action == 'vendor_performance_list':
            return VendorPerformanceSerializer
        return super().get_serializer_class()

    @action(methods=['get'], detail=False, url_path='(?P<vendor_id>[0-9]+)/performance')
    def vendor_performance_list(self, request, vendor_id=None, *args, **kwargs):
        try:
            vendor = vendor_profile.objects.filter(id=vendor_id).first()
            serializer = VendorPerformanceSerializer(vendor, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
