from django.db import models
from drf_yasg.inspectors import SwaggerAutoSchema
# Create your models here.
class CustomAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        tags = self.overrides.get('tags', None) or getattr(self.view, 'my_tags', [])
        if not tags:
            tags = [operation_keys[0]]

        return tags

class vendor_profile(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField(max_length=350)
    address = models.TextField(max_length=350)
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfilment_rate = models.FloatField(default=0.0)
