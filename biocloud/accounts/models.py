from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, related_name='account')
    description = models.TextField(blank=True)

