from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileModelForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.
def signup(request):
    if request.method == 'POST':
        s_form = SignupForm(request.POST)
        if s_form.is_valid():
            s_form.save()
            return redirect('signin')
    else:
        s_form= SignupForm()
    context = {
        's_form' : s_form
    }
    return render(request, 'signup.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'signin.html')


@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')

login_required(login_url='signin')
def profilepage(request):
    user_inst = Profile.objects.all()

    context ={
        'user_inst' : user_inst
    }
    return render(request, 'profile.html', context)


def profileedit(request, pk):
    profile_obj = Profile.objects.get(id = pk)
    if request.method == 'POST':
        form = ProfileModelForm(request.POST, request.FILES, instance=profile_obj)
        if form.is_valid():
            form.save()
            return redirect('profilepage')
    else:
        form = ProfileModelForm(instance=profile_obj)
    context = {
        'form' : form
    }
    return render(request, 'profileedit.html', context)