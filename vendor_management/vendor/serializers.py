from rest_framework import serializers
from vendor.models import vendor_profile

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_profile
        fields = "__all__"

class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_profile
        fields = ('name','contact_details','address','vendor_code')

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_profile
        fields = ('on_time_delivery_rate','quality_rating_avg','average_response_time','fulfilment_rate')