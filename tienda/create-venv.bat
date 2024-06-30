call cd ..
call rmdir /s /q tienda_venv
call py -m venv tienda_venv
call cd tienda_venv
call cd Scripts
call activate
call cd ..
call cd ..
call cd tienda
call pip install -r requirements.txt