from django.apps import AppConfig

class FastfoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fastfood'

    def ready(self):
        import fastfood.signals

