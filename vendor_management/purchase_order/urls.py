from django.urls import path,include
from rest_framework import routers
from purchase_order.views import PurchaseViewset, HistoricalViewset

router = routers.DefaultRouter()
router.register(r'purchase_order',PurchaseViewset),
router.register(r'history_record',HistoricalViewset)


urlpatterns = [
    path('', include(router.urls))
]


