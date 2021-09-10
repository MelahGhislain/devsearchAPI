from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.OneToOneField(User, related_name='owner', on_delete=models.CASCADE, unique=True)
    location = models.CharField(max_length=150)
    bio = models.TextField(max_length=500)
    short_intro = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)# image most have a default
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

