from django.shortcuts import render
from app.models import Labels, Memos
from app.forms import MemoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def memo_list(request):

    nav_check = "sidebar_memo"

    page = int(request.GET.get("p", 1))

    memo_paginator = Paginator(
        Memos.objects.order_by("-created_at").filter(auth="open"), 9)
    memo = memo_paginator.get_page(page)

    return render(request, "memo/list.html", {"nav_check": nav_check, "memo": memo})


@login_required
def memo_create(request):

    nav_check = "sidebar_memo"

    form = MemoForm()

    labels = Labels.objects.all()

    return render(request, "memo/create.html", {"form": form, "labels": labels, "nav_check": nav_check})


def memo_view(request, memo_id):

    nav_check = "sidebar_memo"

    memo = Memos.objects.filter(pk=memo_id)[0]

    if memo.auth == "secret":
        if request.user.id != memo.writer_id:
            return render(request, 'alert.html', {"first": "비공개 게시글입니다.", "times": 1, 'url': '/memo/list'})

    return render(request, "memo/retrieve.html", {"nav_check": nav_check, "memo": memo})


def memo_update(request, memo_id):

    nav_check = "sidebar_memo"
    memo = Memos.objects.filter(pk=memo_id)[0]

    if request.user.id == memo.writer_id:
        labels = Labels.objects.all()

        return render(request, "memo/update.html", {"nav_check": nav_check, "memo": memo, "labels": labels})
    else:
        url = f"/memo/view/{memo.id}"
        return render(
            request, 'alert.html',
            {"first": "본인만 수정이 가능합니다.", "times": 1,
                "second": '다시 시도하여 주세요', 'url': url})
