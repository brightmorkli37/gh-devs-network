from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    short_intro = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True, default='profile_pics/user-default.png'
    )
    address = models.CharField(max_length=100, blank=True, null=True)
    social_twitter = models.URLField(max_length=500, blank=True, null=True)
    social_linkedin = models.URLField(max_length=500, blank=True, null=True)
    social_github = models.URLField(max_length=500, blank=True, null=True)
    social_website = models.URLField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



class Skill(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name