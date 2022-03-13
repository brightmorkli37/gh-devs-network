from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    
    template_name = 'projects/projects.html'
    context = {'projects': projects}
    return render (request, template_name, context)


def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    
    template_name = 'projects/projects_detail.html'
    context = {'project': project}
    return render (request, template_name, context)

def add_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        else:
            form = ProjectForm()
    
    template_name = 'projects/project_form.html'
    context = {'form': form}
    return render (request, template_name, context)

def update_project(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES or None, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        else:
            form = ProjectForm(instance=project)
    
    template_name = 'projects/update_project.html'
    context = {'form': form}
    return render (request, template_name, context)

def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    
    if request.method == 'POST':
        project.delete()
        return redirect ('projects')
        
    
    template_name = 'projects/delete_template.html'
    context = {'object': project}
    return render (request, template_name, context)