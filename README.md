# Proyecto Programación Web

Integrantes:
* Ignacio Peralta 008D i.peralta@duocuc.cl
* José Rivero 008D jo.rivero@duocuc.cl
* Felipe Tapia 008D Fe.tapias@duocuc.cl

## Commands
Virtual enviroment setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tienda/requirements.txt
```
Migrate database
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Run server
```bash
python3 manage.py runserver
```
To populate the database go to ```127.0.0.1:8000/poblar```