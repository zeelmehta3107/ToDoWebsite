from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=50)
    work = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title