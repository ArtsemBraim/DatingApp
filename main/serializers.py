from rest_framework import serializers

from profiles.models import Profile
from .models import Match, Swipe


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'age', 'description']


class SwipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Swipe
        exclude = ['profile1']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swipe
        exclude = ['profile1']
