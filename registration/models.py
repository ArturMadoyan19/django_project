from django.db import models

class Reg(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
