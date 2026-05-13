from django.contrib import admin
from .models import Task

# Регистрируем модель в админке
admin.site.register(Task)