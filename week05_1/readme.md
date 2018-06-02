# Flask
```python
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name='Wasit Limprsert')

# 'ipconfig' to check your pubic ip
# you have to disable firewall or allow incomming connection to the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

# Django
Same concept with a solid structure
## views.py
```python
from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {'name': 'Albert Einstein'})
```

## urls.py
```python
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home')
]
```
