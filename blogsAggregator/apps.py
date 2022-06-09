from django.apps import AppConfig
from django.conf import settings


class BlogsaggregatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogsAggregator'
    verbose_name = 'blogs aggregator'

    def ready(self):
        from .updater import start
        if settings.SCHEDULER_AUTOSTART:
            start()
