from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Payment(models.Model):
    aid = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DateTimeField(default=timezone.now)
    item_code = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    approved_at = models.DateTimeField()
    tid = models.CharField(
        max_length=30,
        null=True
    )
