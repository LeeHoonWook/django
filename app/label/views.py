from django.shortcuts import render, redirect
from app.models import Labels
from app.forms import LabelForm
from django.contrib.auth.decorators import login_required


def label_list(request):

    nav_check = "sidebar_label"

    return render(request, "label/list.html", {"nav_check": nav_check})


@login_required
def label_create(request):

    nav_check = "sidebar_label"

    form = LabelForm()

    labels = Labels.objects.all()

    return render(request, "label/create.html", {"form": form, "labels": labels, "nav_check": nav_check})
