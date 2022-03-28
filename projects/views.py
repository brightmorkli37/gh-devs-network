from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from .forms import ProjectForm
from .utils import searchProjects, paginateProjects


def projects(request):
    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    template_name = 'projects/projects.html'
    context = {
        'projects': projects, 'search_query': search_query,
        'custom_range': custom_range,
    }
    return render (request, template_name, context)


def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    
    template_name = 'projects/projects_detail.html'
    context = {'project': project}
    return render (request, template_name, context)

@login_required(login_url='login')
def add_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user.profile
            # the user can be fetched this other way
            # project = form.save(commit=False)
            # project.owner = request.user
            # project.save()
            form.save()
            if request.user.is_authenticated:
                return redirect('account')
            else:
                return redirect('profiles')
            # return redirect('projects')
        else:
            form = ProjectForm()
    
    template_name = 'projects/project_form.html'
    context = {'form': form}
    return render (request, template_name, context)

@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES or None, instance=project)
        if form.is_valid():
            form.save()
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Project updated successfully')
            if request.user.is_authenticated:
                return redirect('account')
            else:
                return redirect('profiles')
            # return redirect('projects')
        else:
            messages.error(request, 'error occured... check input fields')
            form = ProjectForm(instance=project)
    
    template_name = 'projects/project_form.html'
    context = {'form': form}
    return render (request, template_name, context)

@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully')
        if request.user.is_authenticated:
            return redirect('account')
        else:
            return redirect ('projects')
        
    
    template_name = 'delete_template.html'
    context = {'object': project}
    return render (request, template_name, context)