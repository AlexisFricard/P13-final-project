release: python manage.py migrate
web: gunicorn mastercontrat.wsgi --log-file -
webchat: daphne -p $PORT -b 0.0.0.0 mastercontrat.asgi:application -v2
worker: python manage.py runworker channel_layer -v2