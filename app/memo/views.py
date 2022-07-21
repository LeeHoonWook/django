from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from app.models import Users, Labels
from app.forms import MemoForm
from django.contrib.auth.decorators import login_required


def memo_list(request):

    nav_check = "sidebar_memo"

    return render(request, "memo/list.html", {"nav_check": nav_check})


@login_required
def memo_create(request):

    nav_check = "sidebar_memo"

    form = MemoForm()

    labels = Labels.objects.all()

    return render(request, "memo/create.html", {"form": form, "labels": labels, "nav_check": nav_check})
