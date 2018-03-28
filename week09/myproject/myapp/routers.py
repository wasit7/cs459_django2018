from rest_framework import routers, serializers, viewsets
from myapp.viewsets import CustomerViewSet, CarViewSet, RentViewSet
router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'car', CarViewSet)
router.register(r'rent', RentViewSet)