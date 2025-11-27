from django.urls import path, include

from . import views

urlpatterns = [
    path("", include("users.urls")),
    path("", views.index, name="index"),
]
