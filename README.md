# monedas-sim
Review de codigo.

Objetivo: Realizar una revision del codigo buscando errores de seguridad tanto a nivel de la aplicacion, como de la logica de negocios implementada.

El codigo corresponde a una etapa de evaluacion de los desarrolladores de Ripio, cuyo requerimiento es crear una moneda y simular sus operaciones.

------------------------------------------------------------------------------

Simulación de transferencia de monedas

    1. Crear usuario monedasSim en PostgreSQL, con password 1234
    2. Crear una base monedasSim en PostgreSQL
    3. pip install -r requirements.txt
    4. python manage.py migrate
    5. python manage.py populate_monedas --CREA LAS MONEDAS DISPONIBLES
    6. python manage.py runserver