from django.contrib import admin

from todo_api.models import Todo

@admin.register(Todo)  # Register the model with the Django admin site
class TodoAdmin(admin.ModelAdmin):
    list_display = ['task']
