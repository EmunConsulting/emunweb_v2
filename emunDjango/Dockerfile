FROM python:3.10

WORKDIR /django

ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Copy the entrypoint script and set the permissions
COPY ./entrypoint.sh /emunDjango/entrypoint.sh
RUN chmod +x /emunDjango/entrypoint.sh


# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/emunDjango/entrypoint.sh"]