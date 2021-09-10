from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True , null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    adress = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)# image most have a default
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username
    class Meta:
        ordering = ['-created']

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

