from django.apps import AppConfig


class StrategiesConfig(AppConfig):
    name = 'strategies'

    def ready(self):
        import strategies.signals
