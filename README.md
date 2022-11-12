# PlayWithTamil

## Tech Stack
1. Python 3.8
2. Django 4.1
3. Django REST Framework 3.13
4. ReactJS 18.x


## Django Packages
#### (for installation - pip install virtualenv)
`/django $ virtualenv venv`

#### activate venv
`/django $ source venv/bin/activate`

#### deactivate venv
`/django $ deactivate`

#### Install Django & required packages
`sh
(venv) $ pip install -r requirements.txt
`


#### Freeze requirement
`(venv) /django $ pip freeze > requirements.txt`


#### Migrate models & create superuser 
`sh
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
`

#### Run dev server in port 8002
`sh
(venv) $ python manage.py runserver 8002
`
#### For admin access use below url in browser
`sh
http://127.0.0.1:8002/admin/  (or)  http://yourip:8002/admin  
`

#### ReactJS 
`yarn start`



