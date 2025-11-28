from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.method == "POST":
        # TODO: validate input
        user = User.objects.create_user(
            request["username"],
            request["email"],
            request["password"],
        )
        login(request, user)
        messages.success(request, "Successful registration!")
        return redirect("index")
    else:
        context = {}  # TODO: fill in context 
        return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
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
        context = {}  # TODO: fill in context
        return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return redirect("index")
