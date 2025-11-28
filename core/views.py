from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Home | Track It",
    }  # TODO: add more context like user, etc.
    return render(request, "index.html", context)
