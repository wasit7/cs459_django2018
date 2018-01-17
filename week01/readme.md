# First Rrun Server
```sh
git clone https://github.com/wasit7/cs459_django2018.git
cd cs459_django2018
mkdir week01
django-admin startproject project01
cd project01 
python manage.py runserver 
git add -A
git commit -m "first run server"
```

# Add Superuser
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
