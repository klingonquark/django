# Django Restapi Projekt 

https://yopad.eu/p/django-rest-kurs

## Installationshinweise

lokal wie produktiv die .env-Datei anlegen (siehe env_example)
wird dann in den settings.py eingelesen

## LOKAL
    python -m venv venv
    venv\Scripts\active  / unter linux source venv/bin/activate
    (venv) pip install pip-tools
    (venv)  pip-compile requirements.in
    (venv) pip-compile requirements-dev.in
    (venv) pip-sync requirements*.txt
    python manage.py runserver

## PRODUKTIV
    python -m venv venv
    venv\Scripts\active  / unter linux source venv/bin/activate
    (venv) pip install -r requirements.txt
    (venv) python manage.py runserver


## Projekt anlegen

    venv\Scripts\activate
    (venv) django-admin startproject event_manager
    (venv) cd event_manager
    (venv) python manage.py runserver
    # neue App erstellen (nicht vergessen, in den settings.py eintragen)
    (venv) python manage.py startapp events

## Zusatzinformationen

### Github Repository
https://github.com/klingonquark/django

### Django Docs
https://docs.djangoproject.com/en/5.1/

### Tutorial
https://djangoheroes.friendlybytes.net/

https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

### Django Template Tags
https://docs.djangoproject.com/en/5.1/ref/templates/builtins/

### Login Logout
https://djangoheroes.friendlybytes.net/extended_technics/authentification.html#index-0

### PIP-TOOLS
https://djangoheroes.friendlybytes.net/introduction/installation.html#was-ist-pip-tools


### Konfiguration in Umgebungsvariablen
https://django-environ.readthedocs.io/en/latest/
https://djangoheroes.friendlybytes.net/organisation/organize_settings.html#django-environ