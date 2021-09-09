from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Skill


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(null=False, blank=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('id', 'created',)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ('id', 'created',)

