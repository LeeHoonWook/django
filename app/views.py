from django.shortcuts import render
from app.models import Labels, Memos
from django.core.paginator import Paginator
import datetime


def index(request):

    memo_paginator = Paginator(
        Memos.objects.order_by("-like").filter(auth="open"), 5)
    memo = memo_paginator.get_page(1)

    count = (Memos.objects.all().count(), Labels.objects.all().count())

    now = datetime.datetime.today()
    today = (
        Memos.objects.filter(created_at__date=now).count(),
        Labels.objects.filter(created_at__date=now).count())

    nav_check = "sidebar_main"

    return render(
        request, "main.html",
        {"nav_check": nav_check, "count": count, "memo": memo,
         "today": today})
