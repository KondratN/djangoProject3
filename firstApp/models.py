from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=375)
    address = models.CharField(max_length=200)


class Task(models.Model):
    name = models.CharField(max_length=200)
    deadline = models.IntegerField(default=1)
