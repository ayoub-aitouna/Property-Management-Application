from django.apps import AppConfig
from django.db.models.signals import post_migrate


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'

    def ready(self):
        post_migrate.connect(self.Startup, sender=self)

    def Startup(**kwargs):
        from . import scheduler
        scheduler.startScheduler()
