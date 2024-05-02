from rest_framework import serializers
from purchase_order.models import purchase_order, HistoricalPerformance


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = purchase_order
        fields = "__all__"


class HistoriacalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"