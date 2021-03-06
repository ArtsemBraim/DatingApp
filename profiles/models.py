from django.conf import settings
from django.db import models


class Profile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=True)
    age = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    # image = models.ImageField(upload_to='images/')
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    geolocation_appointment_date = models.DateTimeField(null=True)
