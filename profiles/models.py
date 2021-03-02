from django.db import models
from authentication.models import CustomUser


class GeoData(models.Model):

    longitude = models.FloatField()
    latitude = models.FloatField()
    appointment_date = models.DateTimeField()


class Profile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    age = models.IntegerField()
    description = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/')
    geo_data = models.OneToOneField(GeoData, on_delete=models.CASCADE)
