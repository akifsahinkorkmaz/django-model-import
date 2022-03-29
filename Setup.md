# Setup 

## Virtual Environment :

---
virtualenv package is recommended!

---

Installation:
```bash
pip install virtualenv
``` 

Setup:
```bash
# this will create a virtualenv directory named source
virtualenv source
``` 

Activate:
```bash
# get source directory
cd source

# this will activate it on windows:
scripts\activate

# this will probably activate it for another OS:
# (source is a command/not related with the name of the virtual environment/it's just coincidence):
source bin/activate
```
(for further information: https://virtualenv.pypa.io/en/latest/user_guide.html#activators)


Output should be:
```bash
# source virtualenv activated
(source) C:\...\source>
```

## Django :

---
Django 3.2.12 is used! 

---

Installation:
```bash
# (source) C:\...\source>
pip install django
``` 

Setup project:
```bash
# (source) C:\...\source>
django-admin startproject music_app
``` 
(for further information: https://docs.djangoproject.com/en/4.0/intro/tutorial01/)


Output should be:
```bash
# for source/music_app
│   manage.py
│
└───music_app
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py

```

Setup Django apps:
```bash
# (source) C:\...\source\music_app>
python manage.py startapp music
python manage.py startapp user
python manage.py startapp playlist
``` 

Output should be:
```bash
# for source/music_app
│   manage.py
│
├───music
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   └───migrations
│           __init__.py
│
├───music_app
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__
│
├───playlist
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   └───migrations
│           __init__.py
│
└───user
    │   admin.py
    │   apps.py
    │   models.py
    │   tests.py
    │   views.py
    │   __init__.py
    │
    └───migrations
            __init__.py

```

Adding Django adds to `music_app/settings.py` installed apps:

```python
# Before ---------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# ----------------------

# After ----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django apps
    'music',
    'playlist',
    'user',
]
# ----------------------
```

Make migrations:
```bash
# (source) C:\...\source\music_app>
python manage.py makemigrations
python manage.py migrate
``` 

Create superuser:
```bash
# (source) C:\...\source\music_app>
python manage.py createsuperuser
``` 