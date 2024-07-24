from django.db import models
from django.conf import settings
import datetime


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )