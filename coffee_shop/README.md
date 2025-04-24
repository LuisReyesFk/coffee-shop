# Chart project

Para correr la app debes seguir la siguientes instrucciones en la terminal:

``` sh
cd django_one
python3 manage.py runserver
# Crear entorno virtual
python3 -m venv env

# Activar entorno virtual
source env/bin/activate

# Desactivar entorno virtual
deactivate

# Generar requeriments.txt
pip3 freeze > requeriments.txt

# Instalar dependencias
pip3 install -r requeriments.txt

# Verificar que estemos dentro del entorno virtual
which python3

# run app
psql postgres

# create super user
python3 manage.py createsuperuser
# luis
# admin@admin.com
# finkargo
```