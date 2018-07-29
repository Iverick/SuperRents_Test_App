# Rental App

House Renting platform powered by Django framework. It was created following requirement of a test task


# Prerequisites

You need to have Python3(I used version 3.5.2 for developing), Virtualenvwrapper and PostgreSQL database engine already installed and configured on your machine to run this app.

### Environment Variables

List of required environment variables:

| Variable | Value |
| --- | --- |
| `SECRET_KEY` | Django secret key |


# Setup

### Pull code from a github repo
```
git clone https://github.com/Iverick/rental_app_test_task
```

### Open a main project folder
```
cd rental_app_test_task
```

### Create a virtual environment using virtualenvwrapper
```
mkvirtualenv rental_app
```

### Add secret key to virtualenv

Run ```echo SECRET_KEY='<secret_key_value>' >> .env``` command in terminal.
Open ```~/.virtualenvs/rental_app/bin and add``` path to virtualenv in separate terminal and add ```set -a; source ~/rental_app_test_task/.env; set +a``` command to a postactivate script.

### Installing required dependencies
```
pip install -r requirements.txt
```

### Create a database

Start the PostgreSQL database server and enter the ```psql -U postgres -W``` shell.

In the psql shell enter following commands to create a database and a role with necessary permissions:

```
CREATE DATABASE property_rental_db;
CREATE USER property_rental_db;
GRANT ALL ON DATABASE property_rental_db to "property_rental_db";
ALTER USER property_rental_db PASSWORD 'dev';
ALTER USER property_rental_db CREATEDB;
```

Exit the ```psql``` shell

```
\q
```

### Open a django project folder
```
cd django
```

### Make database migrations
```
python manage.py migrate
```

### Create a superuser so you can login to the admin:
```
python manage.py createsuperuser
```

### Run server
```
python manage.py runserver
```

### List of available web pages
```http://localhost:8000/home/``` home page of an application

```http://localhost:8000/add-property/``` displays a form to submit a property into a database

```http://localhost:8000/vacant-properties/``` displays list of vacant properties

```http://localhost:8000/rented-properties/``` displays list of rented properties

```http://localhost:8000/api/properties/?format=json``` API endpoint to display a list of all properties added to a database
