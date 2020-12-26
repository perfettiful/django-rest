from rest_framework import viewsets

from .serializers import HeroSerializer, ProfileSerializer
from .models import Hero, Profile


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('first_name')
    serializer_class = ProfileSerializer
