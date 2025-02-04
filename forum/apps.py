from django.apps import AppConfig


class ForumConfig(AppConfig):
    """
    ForumConfig class to configure the forum app settings.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'
