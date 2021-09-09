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
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

