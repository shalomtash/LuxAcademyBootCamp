from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    create_date = models.DateTimeField('date published')
