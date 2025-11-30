from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successful registration!")
            return redirect("login")
    else:
        form = RegistrationForm()
    context = {}  # TODO: fill in context (remember to add form) 
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                messages.success(request, "Successful login!")
                return redirect("index")
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Login failed. Please try again.")
    else:
        form = AuthenticationForm()
    context = {}  # TODO: fill in context (remember to add form)
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return redirect("index")
