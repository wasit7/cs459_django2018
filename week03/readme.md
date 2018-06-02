# basic web view-url

## views.py
this file define the responses of requests

## urls.py
managing the routing of request from an url to a view function

```python
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^current_datetime/', views.current_datetime ),
]
