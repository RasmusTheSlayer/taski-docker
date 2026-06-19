"""Модуль конфигурации проекта."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Модуль конфигурации проекта."""

    class Meta:
        """Модуль конфигурации проекта."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
