from django.shortcuts import render, redirect
from users.models import Profile, Skill
from users.forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'username or password is incorrect')

    template_name = 'users/login_register.html'
    context = {'page': page}
    return render(request, template_name, context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'logout succesful')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)   
        if form.is_valid():
            # form.save()
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'User created succesfully')
            return redirect('profiles')
        else:
            messages.error(request, 'User not created... check input fields')
            form = CustomUserCreationForm()

    template_name = 'users/login_register.html'
    context = {'page': page, 'form': form}
    return render(request, template_name, context)

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


@login_required(login_url='login')
def userAccount(request):
    profile = Profile.objects.get(user=request.user)
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    template_name = 'users/account.html'
    context = {
        'profile': profile, 'skills': skills, 'projects': projects,
    }
    return render(request, template_name, context)

@login_required(login_url='login')
def editProfile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully')
            return redirect('account')
        else:
            messages.error(request, 'Profile not updated... check input fields')
            form = ProfileForm(instance=profile)

    template_name = 'users/edit-profile.html'
    context = {'form': form}
    return render (request,template_name, context)

@login_required(login_url='login')
def addSkill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user.profile
            form.save()
            messages.success(request, 'Skill added succesfully')
            return redirect('account')
        else:
            messages.error(request, 'Skill not added... check input fields')
            form = SkillForm()

    template_name = 'users/skill-form.html'
    context = {'form': form}
    return render (request,template_name, context)

@login_required(login_url='login')
def updateSkill(request, pk):
    skill = Skill.objects.get(pk=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.instance.owner = request.user.profile
            form.save()
            messages.success(request, 'Skill updated succesfully')
            return redirect('account')
        else:
            messages.error(request, 'Skill not updated... check input fields')
            form = SkillForm()

    template_name = 'users/skill-form.html'
    context = {'form': form}
    return render (request,template_name, context)

@login_required(login_url='login')
def deleteSkill(request, pk):
    skill = Skill.objects.get(pk=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'skill deleted')
        return redirect('account')
    
    template_name = 'delete_template.html'
    context = {'object': skill}
    return render (request,template_name, context)