"""Модуль конфигурации проекта."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Модуль конфигурации проекта."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
