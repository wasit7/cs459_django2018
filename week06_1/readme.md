# Server static files
## urls.py
```python

from django.urls import path

urlpatterns = [
   path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

## File structure

```sh
wasitVision/static_demo: tree -F
.
└── myproject/
    ├── db.sqlite3
    ├── manage.py*
    ├── media/
    │   ├── cars/
    │   │   └── Screenshot_from_2018-02-12_12-36-29.png
    │   └── media.gif
    ├── myapp/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_auto_20180228_0741.py
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   │       ├── 0001_initial.cpython-35.pyc
    │   │       ├── 0002_auto_20180228_0741.cpython-35.pyc
    │   │       └── __init__.cpython-35.pyc
    │   ├── models.py
    │   ├── __pycache__/
    │   │   ├── admin.cpython-35.pyc
    │   │   ├── __init__.cpython-35.pyc
    │   │   └── models.cpython-35.pyc
    │   ├── tests.py
    │   └── views.py
    ├── myproject/
    │   ├── __init__.py
    │   ├── __pycache__/
    │   │   ├── __init__.cpython-35.pyc
    │   │   ├── settings.cpython-35.pyc
    │   │   ├── urls.cpython-35.pyc
    │   │   └── wsgi.cpython-35.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── static/
        └── hello.txt

10 directories, 28 files

```
