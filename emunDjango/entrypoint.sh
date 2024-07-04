#!/bin/sh
#
## Wait for the database to be ready
#while ! nc -z $DATABASE_HOST 3306; do
#  echo "Waiting for the MySQL database to be ready..."
#  sleep 1
#done

# Run migrations
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

# Create superuser if it doesn't exist
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
EOF

# Create groups if they don't exist
python manage.py shell <<EOF
from django.contrib.auth.models import Group
groups = ["admin", "moderator", "facilitator", "traveler"]
for group in groups:
    if not Group.objects.filter(name=group).exists():
        Group.objects.create(name=group)

# Assign admin to "admin" group
admin = User.objects.get(username='admin')
admin_group = Group.objects.get(name='admin')
admin.groups.add(admin_group)
EOF

# Start the Django server
exec "$@"
