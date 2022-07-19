from django import forms
from app.models import Users
from argon2 import PasswordHasher, exceptions  # pip install argon2-cffi
from django.contrib.auth import login
from django.shortcuts import redirect

from app.errors import PasswordMatchError


class RegisterForm(forms.Form):
    user_id = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(attrs={
            "id": "username", "class": "form-control",
            "placeholder": "아이디를 입력해주세요",
            "autofocus": "autofocus", "minlength": 4}))

    password = forms.CharField(
        max_length=100, required=True,
        widget=forms.PasswordInput(attrs={
            "id": "password", "class": "form-control",
            "placeholder": "비밀번호를 입력해주세요",
            "aria-describedby": "password", "autocomplete": "off", "minlength": 4}))

    check_password = forms.CharField(
        max_length=100, required=True,
        widget=forms.PasswordInput(attrs={
            "id": "check_password", "class": "form-control",
            "placeholder": "비밀번호를 한번 더 입력해주세요",
            "aria-describedby": "password", "autocomplete": "off", "minlength": 4}))

    hint = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "비밀번호 답변 (꼭 기억해주세요)"}))

    check = forms.CharField(
        max_length=100, required=True,
        widget=forms.HiddenInput(attrs={
            "id": "checker", "class": "form-control", "value": "False"}))

    def save(self, data, request):
        user_id = data.get('user_id')
        pw = data.get('password')
        check_pw = data.get('check_password')
        hint = data.get('hint')
        check = data.get('check')

        if check == 'False':
            msg = '아이디 중복확인이 되지 않았습니다.'
        else:
            try:
                if pw != check_pw:
                    raise PasswordMatchError
                else:
                    user = Users(
                        username=user_id,
                        password=PasswordHasher().hash(pw),
                        hint=hint,
                        user_auth="MEMBER")
                    user.save()
                    login(request, user)
                    msg = '성공'

            except PasswordMatchError as e:
                msg = e

        return msg


class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(attrs={
            "id": "username", "class": "form-control",
            "placeholder": "아이디를 입력해주세요",
            "autofocus": "autofocus", "minlength": 4}))

    password = forms.CharField(
        max_length=100, required=True,
        widget=forms.PasswordInput(attrs={
            "id": "password", "class": "form-control",
            "placeholder": "비밀번호를 입력해주세요",
            "aria-describedby": "password", "autocomplete": "off", "minlength": 4}))

    def login(self, data, request):
        user_id = data.get('user_id')
        pw = data.get('password')
        msg = "올바른 유저ID와 패스워드를 입력하세요."
        try:
            user = Users.objects.get(username=user_id)
        except Users.DoesNotExist:
            pass
        else:
            try:
                PasswordHasher().verify(user.password, pw)
            except exceptions.VerifyMismatchError:
                pass
            else:
                login(request, user)
                msg = '성공'

        return msg


class FindForm(forms.Form):
    user_id = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(attrs={
            "id": "username", "class": "form-control",
            "placeholder": "아이디를 입력해주세요",
            "autofocus": "autofocus", "minlength": 4}))

    hint = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control", "placeholder": "비밀번호 답변"}))

    def check(self, data, request):
        user_id = data.get('user_id')
        hint = data.get('hint')
        msg = "일치하지 않습니다."
        try:
            user = Users.objects.get(username=user_id)
        except Users.DoesNotExist:
            pass
        else:
            if user.hint != hint:
                pass
            else:
                user.password = PasswordHasher().hash('1234')
                user.save()
                msg = '성공'

        return msg
