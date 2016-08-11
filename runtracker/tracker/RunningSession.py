from django.db import models
from django.conf import settings

class RunningSession(models.Model):
    """Development iteration period."""

    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    duration = models.FloatField()
    miles = models.FloatField()
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)