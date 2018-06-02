# REST API

## routers.py
```python
from rest_framework import routers, serializers, viewsets
from myapp.viewsets import CustomerViewSet, CarViewSet, RentViewSet
router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'car', CarViewSet)
router.register(r'rent', RentViewSet)
```

## serializers.py
```pyython

from myapp.models import Customer, Car, Rent
from rest_framework import routers, serializers, viewsets


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'
```

## viewsets.py
```python
from rest_framework import routers, serializers, viewsets
from myapp.models import Customer, Car, Rent 
from myapp.serializers import CustomerSerializer, CarSerializer, RentSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
```
