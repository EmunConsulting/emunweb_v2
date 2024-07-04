FROM python:3.10

WORKDIR /django

ENV PYTHONUNBUFFERED=1

# Install netcat
RUN apt-get update && apt-get install -y netcat

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files
COPY . .

# Wait for the database to be ready
CMD while ! nc -z $DATABASE_HOST 3306; do \
      echo "Waiting for the MySQL database to be ready..."; \
      sleep 1; \
    done && \
    # Run migrations
    python manage.py migrate && \
    # Create superuser if it doesn't exist
    python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); if not User.objects.filter(username='admin').exists(): User.objects.create_superuser('admin', 'admin@example.com', 'admin')" && \
    # Create groups if they don't exist
    python manage.py shell -c "from django.contrib.auth.models import Group; groups = ['admin', 'moderator', 'facilitator', 'traveler']; for group in groups: if not Group.objects.filter(name=group).exists(): Group.objects.create(name=group)" && \
    # Assign admin to "admin" group
    python manage.py shell -c "from django.contrib.auth import get_user_model; from django.contrib.auth.models import Group; User = get_user_model(); admin = User.objects.get(username='admin'); admin_group = Group.objects.get(name='admin'); admin.groups.add(admin_group)" && \
    # Start the Django server
    python manage.py runserver 0.0.0.0:8000
