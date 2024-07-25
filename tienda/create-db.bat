call cd ..
call cd tienda_venv
call cd Scripts
call activate
call cd ..
call cd ..
call cd tienda
call py manage.py makemigrations
call py manage.py migrate