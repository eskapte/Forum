from django.apps import AppConfig


class LamersroomConfig(AppConfig):
    name = 'Lamersroom'

    def ready(self):
        import Lamersroom.signals.handlers