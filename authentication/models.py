from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, subscription_type, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            subscription_type=subscription_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, subscription_type, password=None):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            subscription_type=subscription_type,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    SUBSCRIPTION_TYPE_CHOICES = [
        (0, 'Basic'),
        (1, 'VIP'),
        (2, 'Premium')
    ]

    subscription_type = models.IntegerField(
        choices=SUBSCRIPTION_TYPE_CHOICES,
        default=0
    )

    objects = CustomUserManager()
