# Django Restapi Projekt 


## Installationshinweise

lokal wie produktiv die .env-Datei anlegen (siehe env_example)
wird dann in den settings.py eingelesen

## LOKAL
    python -m venv venv
    venv\Scripts\active  / unter linux source venv/bin/activate
    (venv) pip install pip-tools
    pip-compile requirements.in
    pip-compile requirements-dev.in
    pip-sync requirements*.txt

## PRODUKTIV
    python -m venv venv
    venv\Scripts\active  / unter linux source venv/bin/activate
    (venv) pip install -r requirements.txt



## Projekt anlegen

    venv\Scripts\activate
    (venv) django-admin startproject event_manager
    (venv) cd event_manager
    (venv) python manage.py runserver
    (venv) python manage.py startapp events