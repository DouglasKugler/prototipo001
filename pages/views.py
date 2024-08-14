from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def home(request):
    if request.user.is_authenticated:
        return redirect('principal')
    return render(request, 'pages/home.html')
def login(request):
    return render(request, 'pages/registration/login.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('principal')
        else:
            form = UserCreationForm()
    else:
        return render(request, 'pages/registration/register.html', {'form': form})

#def logout(request):
#    return render(request, 'pages/logout.html')
@login_required
def principal(request):
    return render(request, 'pages/principal.html')
def profile(request):
    return render(request, 'pages/principal.html')
def proposta(request):
    return render(request, 'pages/grup1/teste01.html')

