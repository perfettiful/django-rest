from rest_framework import serializers

from .models import Hero
from .models import Profile


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'personal_statement', 'resume_url' )

