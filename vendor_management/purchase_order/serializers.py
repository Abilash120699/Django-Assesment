from rest_framework import serializers
from purchase_order.models import purchase_order


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = purchase_order
        fields = "__all__"