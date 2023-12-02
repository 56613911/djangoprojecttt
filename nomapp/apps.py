from django.apps import AppConfig


class NomappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nomapp'




    def ready(self):
        import nomapp.signals  # This line connects your signals file

