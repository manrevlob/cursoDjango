from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user_auth.forms import SignUpForm

# Create your views here.
def index(request):
    auth = True
    if not request.user.is_authenticated:
        auth = False
    return render(request, 'index.html', {'auth':auth})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(is_staff=True, is_active=True, **form.cleaned_data)
            messages.success(request, "Usuario creado satisfactoriamente")
            if login_user(request, user):
                return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def login_user(request, user):
    login(request, user)
    return True

def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Por favor, comprueba tu usuario y contraseña")
    return render(request, 'login.html')

@login_required(redirect_field_name='login')
def change_password(request):
    if request.POST:
        user = request.user
        password = request.POST.get('password', None)
        if password:
            user.set_password(password)
            user.save()
        return redirect('index')
    return render(request, 'change_password.html')

def logout_user(request):
    logout(request)
    return redirect('login')
    