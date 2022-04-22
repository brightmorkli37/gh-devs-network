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
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Full Name')
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    short_intro = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True, default='profile_pics/user-default.png'
    )
    address = models.CharField(max_length=100, blank=True, null=True)
    social_twitter = models.CharField(max_length=500, blank=True, null=True)
    social_linkedin = models.CharField(max_length=500, blank=True, null=True)
    social_github = models.CharField(max_length=500, blank=True, null=True)
    social_website = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username



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


class Message(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages'
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']

