from django.apps import AppConfig


class BlogsaggregatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogsAggregator'
    verbose_name = 'blogs aggregator'

    def ready(self):
        from .updater import start
        start()
