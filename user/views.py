from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, f'Invalid username or password')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})

@login_required
def dashboard(request):
    if request.user.role == 1:
        return render(request, 'admin.html',{'name':request.user})
    
@login_required
def Logout(request):
    logout(request)
    return redirect('/')
    