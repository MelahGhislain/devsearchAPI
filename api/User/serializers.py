from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Skill


class RegisterSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    password2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ('user', 'first_name', 'last_name',
                  'username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, obj):
        """ checks if both password match else returns an error"""

        password1 = obj.get('password')
        password2 = obj.get('password2')
        if password1 != password2:
            raise serializers.ValidationError(
                {"Password": "Passwords don't match"})

        return super().validate(obj)

    def create(self, validated_data):
        """ creates a new user"""
        return User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'], first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['skills', 'adress', 'bio', 'short_intro',
                  'picture', 'github', 'linkedin', 'twitter',
                  'youtube', 'website']

    # def create(self, validated_data):
    #     pass
