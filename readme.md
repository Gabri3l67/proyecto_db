# Create virtual env
`python -m venv env`

# Activate virtual env
`source env/bin/activate`

# Installing dependencies
`pip install -r requirements.txt`

# Create app
`python manage.py startapp shopApp`

# Run server in development
`python manage.py runserver 3080`

# Run server in production mode
In shop/settings.py set `DEBUG=FALSE`, then

`gunicorn shop.wsgi:application --bind 0.0.0.0:3080`

# Create admin user
`python manage.py createsuperuser`

# Tasks

## Daniel
[] Django

## Ale

[] Indices
- Producto_nombres
- cliente_email
- pedidos-fechapedido

## Luis

[] Vista Cliente Pedidos
[] Procedimiento almacenado con transaccion de Registrar pedido
[] Disparador auditoria productos