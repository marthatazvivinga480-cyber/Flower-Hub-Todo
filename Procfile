web: python manage.py migrate --noinput && gunicorn todoproject.wsgi:application --bind 0.0.0.0:${PORT:-8000} --log-file -
