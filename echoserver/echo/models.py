from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    genre = models.CharField(max_length=50)
    public_date = models.IntegerField()
    publisher = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE_CHOICES = (
        ('standard', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='standard')