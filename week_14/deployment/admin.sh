#!/bin/bash
docker exec -it web1 python manage.py createsuperuser --username admin --email e@mail.com
