from django.apps import AppConfig


class VisaapplicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visaapplications'

    def ready(self):
        import visaapplications.signals  # Ensure to import the signals module
