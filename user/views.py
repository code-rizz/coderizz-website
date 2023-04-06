from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Projects
from .models import User

# Create your views here.


@login_required
def dashboard(request):
    if request.user.role == 1:
        print(f"h:{request.user.password}") 
        user = request.user
        users = User.objects.all()
        no_admin = len(users.filter(role = 1))
        no_modrator = len(users.filter(role = 2))
        no_member = len(users.filter(role = 3))
        no_user = len(users)
        return render(request, 'admin-dashboard.html',locals())
    
@login_required
def project(request):
    if request.user.role == 1:
        projects = enumerate(Projects.objects.all())
        return render(request, 'admin-project.html',{'projects':projects})


@login_required
def del_project(request, id):
    if request.user.role == 1:
        try:
            p = Projects.objects.all()[id]
            p.delete()
        except Exception as e:
            print(e)
        return redirect('projects')
    
@login_required
def add_project(request):
    if request.user.role == 1:            
        if request.method ==   "POST":
            name = request.POST['name']
            details = request.POST['details']
            url = request.POST['url']
            p = Projects(project_name=name, project_description=details,project_link=url)
            p.save()
        return redirect("projects")