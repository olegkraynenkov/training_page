from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', blank=True)
