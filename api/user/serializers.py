from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(null=False, blank=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        