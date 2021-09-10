from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Skill

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, obj):
        password1 = obj.get('password')
        password2 = obj.get('password2')
        if password1 != password2:
            raise serializers.ValidationError(
                {"Password": "Passwords don't match"})

        return super().validate(obj)

    def create(self, validated_data):
        return User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    # def create(self, validated_data):
    #     pass

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
