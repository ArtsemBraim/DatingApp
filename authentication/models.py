from profiles.models import Profile

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, subscription_type=0, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            subscription_type=subscription_type
        )

        user.set_password(password)
        user.save(using=self._db)
        Profile.objects.create(user=user)

        return user

    def create_superuser(self, username, email, subscription_type=2, password=None):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            subscription_type=subscription_type,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class Subscription(models.Model):

    name = models.CharField(max_length=20)
    is_inf_swipes = models.BooleanField()
    swipe_count = models.IntegerField()
    default_radius = models.IntegerField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    subscription = models.ForeignKey(Subscription, on_delete=models.PROTECT)
    objects = CustomUserManager()


class CustomRadius(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    radius = models.IntegerField()
