from django.db import models
from djongo import models as djongo_models


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Product(djongo_models.Model):
    name = models.CharField(max_length=100)
    attributes = djongo_models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
