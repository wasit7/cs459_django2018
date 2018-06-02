
# Basic ORM

```sh
python manage.py shell_plus --notebook
```

# Create a Class diagrage
To create a diagram please read a documents of django-extensions [here](http://django-extensions.readthedocs.io/en/latest/graph_models.html).

```sh
python ./manage.py graph_models --pydot -a -g -o others/classdiagram.png

```


# select all cars


```python
Car.objects.all()
#ORM: Object Relational mapping
```




    <QuerySet [<Car: id: 1, model: Vios, price: 500000>, <Car: id: 2, model: Camry, price: 800000>, <Car: id: 3, model: Jazz, price: 400000>]>




```python
print(Car.objects.all().query)
```

    SELECT "myapp_car"."id", "myapp_car"."model", "myapp_car"."detail", "myapp_car"."price" FROM "myapp_car"



```python
for i in Car.objects.all():
    print(i.model, i.detail, i.price)
```

    Vios medium price 500000
    Camry High price 800000
    Jazz low price entry car 400000


# get a car by id


```python
Customer.objects.get(id=1)
```




    <Customer: id: 1, Albert>



# get cars by filter


```python
Car.objects.filter(price__lte=500000)
```




    <QuerySet [<Car: id: 1, model: Vios, price: 500000>, <Car: id: 3, model: Jazz, price: 400000>]>




```python
Car.objects.filter(price=500000)
```




    <QuerySet [<Car: id: 1, model: Vios, price: 500000>]>




```python
Car.objects.filter(price__gt=500000)
```




    <QuerySet [<Car: id: 2, model: Camry, price: 800000>]>




```python
print( Car.objects.filter(price__gte=500000).query )
```

    SELECT "myapp_car"."id", "myapp_car"."model", "myapp_car"."detail", "myapp_car"."price" FROM "myapp_car" WHERE "myapp_car"."price" >= 500000


# Relation
ORM can resolve forward and reward relation

## Car
<img src="others/car.png",width=500>

## Customer
<img src="others/customer.png",width=500>

## Rent
<img src="others/rent.png",width=500>


```python
Rent.objects.get(id=2).car
```




    <Car: id: 3, model: Jazz, price: 400000>




```python
Rent.objects.get(id=2).customer
```




    <Customer: id: 2, Wasit>




```python
Rent.objects.filter(car__price__lte=400000)
```




    <QuerySet [<Rent: Rent object (2)>]>




```python
Rent.objects.filter(car__price__lte=500000)
```




    <QuerySet [<Rent: Rent object (1)>, <Rent: Rent object (2)>]>




```python
Rent.objects.filter(car__price__lte=500000, customer__first_name='Albert') #AND conjuntion
```




    <QuerySet [<Rent: Rent object (1)>]>


