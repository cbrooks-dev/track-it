from django.shortcuts import render

# Create your views here.
def register(request):
    context = {
        "title": "Register | Track It",
    }
    return render(request, "register.html", context)


def login(request):
    context = {
        "title": "Login | Track It",
    }
    return render(request, "login.html", context)


def logout(request):
    context = {
        "title": "Logout | Track It",
    }
    return render(request, "logout.html", context)
