from django.db import models
from django.utils import timezone

from profiles.models import Profile
# Create your models here.


class Swipe(models.Model):
    REACTION_CHOICES = (
        ('L', 'Like'),
        ('D', 'Dislike')
    )

    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=1, choices=REACTION_CHOICES)
    reaction_datetime = models.DateTimeField(default=timezone.now())


class Match(models.Model):
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE)
