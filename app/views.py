from django.shortcuts import render


def index(request):

    nav_check = "sidebar_main"

    return render(request, "main.html", {"nav_check": nav_check})
