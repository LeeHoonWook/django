from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from app.models import Users
from app.forms import LoginForm, RegisterForm, FindForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."
        status_code = 422
        if form.is_valid():
            res = form.save(form.cleaned_data, request)
            msg = res[0]
            status_code = res[1]
            if msg == '성공':
                return render(
                    request, 'alert.html',
                    {"first": "회원가입이 완료", "times": 1,
                     "second": '로그인 중 입니다.', 'url': "/"})
    else:
        msg = None
        status_code = 200
        form = RegisterForm()

    return render(request, "user/register.html", {"form": form, "msg": msg}, status=status_code)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        msg = "올바른 유저ID와 패스워드를 입력하세요."
        status_code = 422
        if form.is_valid():
            res = form.login(form.cleaned_data, request)
            msg = res[0]
            status_code = res[1]

            if msg == '성공':
                return redirect(request.GET.get("next") or "/")
    else:
        msg = None
        status_code = 200
        form = LoginForm()

    return render(request, "user/login.html", {"form": form, "msg": msg}, status=status_code)


def logout_view(request):
    logout(request)

    return redirect("login")


def user_check(request):
    username = request.GET.get("username")
    try:
        Users.objects.get(username=username)

        msg = '현재 등록된 아이디입니다.'
        check = 'error'

    except Exception:
        if username == '':
            msg = '아이디를 입력해주세요'
            check = 'warning'
        elif len(username) < 4:
            msg = '반드시 4자 이상이여야 합니다.'
            check = 'warning'
        else:
            msg = '가입 가능한 아이디입니다.'
            check = 'success'
            return JsonResponse(status=200, data=dict(msg=msg, check=check, username=username), safe=False)

    return JsonResponse(status=422, data=dict(msg=msg, check=check), safe=False)


def user_find(request):
    if request.method == "POST":
        form = FindForm(request.POST)
        msg = "일치하지 않습니다."
        if form.is_valid():
            res = form.check(form.cleaned_data, request)
            msg = res[0]
            random_number = res[1]
            if msg == '성공':
                return render(
                    request, 'alert.html',
                    {"first": "초기화 비밀번호는 ", "times": 3,
                     "second": '다음엔 꼭 기억해주세요', 'url': "login",
                     "random_number": random_number})
    else:
        msg = None
        form = FindForm()

    return render(request, "user/find.html", {"form": form, "msg": msg})
