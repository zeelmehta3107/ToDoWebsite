from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display= ('id', 'username', 'title', 'is_completed')
    list_filter= ('username', 'is_completed', )