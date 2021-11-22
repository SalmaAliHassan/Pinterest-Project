from django.apps import AppConfig


class PinterestConfig(AppConfig):
    name = 'pinterest'

    def ready(self):
        from . import signals