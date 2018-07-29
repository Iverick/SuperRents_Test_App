## Setting up a posgresql database

CREATE DATABASE property_rental_db;
CREATE USER property_rental_db;
GRANT ALL ON DATABASE property_rental_db to "property_rental_db";
ALTER USER property_rental_db PASSWORD 'dev';
ALTER USER property_rental_db CREATEDB;


## Rent App

Simple Django House Renting app


## Setup

### Pulling code from github repo
```
git clone https://github.com/Iverick/rental_app_test_task
```

### Opening a main project folder
```
cd rental_app
```

### Running a virtual environment
```
python3 -m venv .env
source .env/bin/activate
```
(You may also use ```virtualenvwrapper``` which is actually a preferred option)

### Installing required dependencies
```
pip install -r requirements.txt
```

### Opening a django project folder
```
cd django
```

### Making migrations
```
python manage.py migrate
```

### Running server
```
python manage.py runserver
```

## Environment Variables

List of required environment variables:

| Variable | Value |
| --- | --- |
| `SECRET_KEY` | Django secret key |

You can use two ways to set environment variables: via Pycharm or via ```virtualenvwrapper``` scripts.
