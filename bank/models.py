from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Passwords should ideally be hashed!

# Create your models here.