from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import purchase_order, HistoricalPerformance
from .views import (
    ontime_delivery,
    quality_rating_average,
    calculate_average_response_time,
    calculate_fulfillment_rate
)


@receiver(post_save, sender=purchase_order)
def update_vendor_performance(sender, instance, **kwargs):
    vendor = instance.vendor

    vendor.on_time_delivery_rate = ontime_delivery(vendor)
    vendor.quality_rating_avg = quality_rating_average(vendor)
    vendor.average_response_time = calculate_average_response_time(vendor)
    vendor.fulfillment_rate = calculate_fulfillment_rate(vendor)

    HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=ontime_delivery(vendor),
        quality_rating_avg=quality_rating_average(vendor),
        average_response_time=calculate_average_response_time(vendor),
        fulfillment_rate=calculate_fulfillment_rate(vendor),
    )

    vendor.save()
