from django.contrib import admin
from .models import Todolist


@admin.register(Todolist)
class Todolist(admin.ModelAdmin):
    list_display = ['item', 'status', 'created_at']
