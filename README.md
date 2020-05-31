# FullThrottleLabsTestCode: A Backend Test Django Project

## Setup guide
1. Fork and Clone this Repo.
2. Make a virtual environment and activate it. (Refer [virtualenv](https://pypi.org/project/virtualenv/) doc)
3. Install dependencies by running command `pip install -r requirements.txt`
4. Go to inside the project root folder and run the server by the command `./manage.py runserver 0:8000`
5. Open `localhost:8000/api/doc/` in your browser and cheers !!!.


## API List

 1. **Get All Users List**

    url : ***/api/users-list/***

 3. **Populate dummy users data  API**

    url : ***/api/reset-users/***
    or
    **Populate dummy users data by management command**

    This command resets users data and populates new.
    (`./manage.py reset-users-data`)

    dummy users count: 10 (harcoded) 
    
    per-user dummy activity periods count: random 1-5 (harcoded)

## API documentation
Used external library swagger([django-rest-swagger](https://pypi.org/project/django-rest-swagger/)) for API documentation. 

**Links**

 - A swagger-ui view of API specification 

url: ***/api/doc/*** 

- A ReDoc view of API specification

url: ***/api/uidoc/*** 

## Adminpanel Link
Link of django administration page

url: ***/admin/***

username: admin

password: admin

## External installed packages:
Mixer: https://github.com/klen/mixer

Swagger: https://pypi.org/project/django-rest-swagger/

Django Rest: https://pypi.org/project/djangorestframework/


----------------------------------

## Versions
Python: 3.7.5

Django: 3.0.6