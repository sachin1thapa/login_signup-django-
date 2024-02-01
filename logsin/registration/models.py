from django.db import models

# from django import forms 

# Create your models here.

class Userdata(models.Model):
    name = models.TextField(max_length = 20 )
    email = models.EmailField(unique=True)
    password = models.TextField(max_length = 32)


