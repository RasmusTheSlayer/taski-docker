"""Модуль конфигурации проекта."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Модуль конфигурации проекта."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
