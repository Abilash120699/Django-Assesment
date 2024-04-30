from django.urls import path, include
from rest_framework import routers
from vendor.views import VendorViewset

router = routers.DefaultRouter()
router.register(r'vendor', VendorViewset),


urlpatterns = [
    path('', include(router.urls)),
]
