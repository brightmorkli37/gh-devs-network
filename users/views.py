from django.shortcuts import render
from users.models import Profile


def profiles(request):
    profiles = Profile.objects.all()

    template_name = 'users/profiles.html'
    context = {'profiles': profiles}
    return render(request, template_name, context)


def userProfile(request, pk):
    profile = Profile.objects.get(pk=pk)

    # mainSkills is the skills with description
    # otherSkills is the skills without description
    mainSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")


    template_name = 'users/user-profile.html'
    context = {
        'profile': profile,
        'mainSkills': mainSkills,
        'otherSkills': otherSkills,
    }
    return render(request, template_name, context)