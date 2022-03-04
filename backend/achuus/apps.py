from django.apps import AppConfig
from django.core.signals import request_finished

class AchuusConfig(AppConfig):
    name = 'achuus'

    def ready(self):
        from .import signals
        
        
        request_finished.connect(signals.create_profile)
