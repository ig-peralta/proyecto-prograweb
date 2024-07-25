call cd ..
call cd tienda_venv
call cd Scripts
call activate
call cd ..
call cd ..
call cd tienda
call code .
call start chrome http://127.0.0.1:8000/
call py manage.py runserver