from django.urls import path,include
from rest_framework import routers
from purchase_order.views import PurchaseViewset

router = routers.DefaultRouter()
router.register(r'purchase_order',PurchaseViewset),


urlpatterns = [
    path('', include(router.urls))
]


