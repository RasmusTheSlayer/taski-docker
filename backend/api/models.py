"""Модуль конфигурации проекта."""
from django.db import models


class Task(models.Model):
    """Модуль конфигурации проекта."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
