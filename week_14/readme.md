## docker-compose.yml
```yaml
version: '3.5'

services:
  db:
    container_name: postgres_testcompose
    build: ./postgres
    restart: always

  web1:
    container_name: web1_testcompose
    build: ./myproject
    command: sh /code/run.sh
    ports:
      - 8000:8000
    volumes:
      - ./myproject:/code
    depends_on:
      - db
```
## /postgres/Dockerfile
```yaml
FROM postgres
```

## /myproject/Dockerfile
```yaml
FROM python:3
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
```
