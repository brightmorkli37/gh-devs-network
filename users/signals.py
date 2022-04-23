# see below to see how receiver is used with signal functions
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile


# use the receiver function to connect the signal to the function
# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=instance,
            username=user.username,
            email = user.email,
            name = user.first_name + ' ' + user.last_name,

        )

        send_mail(
            subject = 'Welcome to GH Developers Network',
            message = 'Together we build Africa\'s Technology',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [profile.email],
            fail_silently = False,
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        name = profile.name
        name = name.split()
        user.first_name = name[0]
        user.last_name = name[-1]
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# not needed when using the receiver decorator
post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteProfile, sender=Profile)