from django.db import models


class Message(models.Model):
    email = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=None)
    update_date = models.DateTimeField(default=None)
