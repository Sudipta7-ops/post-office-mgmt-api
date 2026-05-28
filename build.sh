#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate
python manage.py shell -c "
from accounts.models import User
if not User.objects.filter(employee_id='EMP001').exists():
    User.objects.create_superuser(employee_id='EMP001', username='admin', password='admin123', email='admin@postoffice.com')
    print('Superuser created')
else:
    print('Superuser already exists')
"