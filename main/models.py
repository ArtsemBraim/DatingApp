from django.db import models
from django.utils import timezone

from profiles.models import Profile
# Create your models here.


class Swipe(models.Model):
    LIKE = 'L'
    DISLIKE = 'D'
    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    )

    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='your_swipes')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='swipes_upon_you')
    reaction = models.CharField(max_length=1, choices=REACTION_CHOICES)
    reaction_datetime = models.DateTimeField(default=timezone.now)

    @staticmethod
    def are_there_swipes_left(profile):
        subscription = profile.user.subscription
        swipes_count = profile.your_swipes.filter(reaction_datetime__date=timezone.now().today()).count()
        return subscription.is_inf_swipes or swipes_count < subscription.swipe_count

    def is_match(self):
        swipe_upon_you = self.profile2.your_swipes.filter(profile2=self.profile1, reaction=self.LIKE)
        return self.reaction == self.LIKE and swipe_upon_you.count() != 0


class Match(models.Model):
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='your_matches')
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='matches_upon_you')
