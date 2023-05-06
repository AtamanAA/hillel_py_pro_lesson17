from datetime import datetime

from django.db import models
from django.utils import timezone


class Log(models.Model):
    execution_time = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    request_path = models.CharField(max_length=100)
    request_method = models.CharField(max_length=40)
