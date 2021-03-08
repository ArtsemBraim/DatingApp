from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Match, Swipe
from .serializers import ProfileListSerializer, SwipeSerializer
from profiles.models import Profile

# Create your views here.


class ProfileListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileListSerializer(profiles, many=True)
        return Response(serializer.data)


class SwipeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SwipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile1=self.request.user.profile)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
