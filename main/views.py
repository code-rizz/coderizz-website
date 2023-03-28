from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from .models import Projects
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.models import User

# Create your views here.
def index(request):
    myProject = Projects.objects.all()
    no_of_projects = len(myProject)
    users = len(User.objects.all())
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            "coderizz: "+name,
            "from:"+name+"\n"+message+"\nreply to: "+email,
            email,
            [
            'coderizz@protonmail.com'
            ],
        )
        return render(request,'index.html',locals())
    else:
        return render(request,'index.html',locals())
def events(request):
    return render(request,'events.html')
def ide(request):
    return render(request,'ide.html')

def update(request):
    myProject = enumerate(Projects.objects.all())
    if request.GET.get('pass', '') == "admin":
        if request.method == "GET":
            if request.GET.get('del', ''):
                try:
                    p  = Projects.objects.all()[int(request.GET.get('del', ''))]
                    p.delete()
                    return render(request,'update.html',locals())
                except Exception as e:
                    return HttpResponse(e)
            else:
                return render(request,'update.html',locals())
        elif request.method == "POST":
            name = request.POST['name']
            details = request.POST['details']
            url = request.POST['url']
            p = Projects(project_name=name, project_description=details,project_link=url)
            p.save()
            
            return render(request,'update.html',locals())
    else:
        return HttpResponse("not allowed")
    
def Login(request):
    if request.method == 'GET' and request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            if "next" in request.GET.keys():
                next = request.GET['next']
                return redirect(next)
            return redirect('dashboard')
        else:
            messages.warning(request, f'Invalid username or password')
    return render(request, 'login.html')


@login_required
def Logout(request):
    logout(request)
    return redirect('/')
    