from django import forms
from app.models import Users
from argon2 import PasswordHasher, exceptions  # pip install argon2-cffi
from django.contrib.auth import login
from django.shortcuts import redirect

from app.errors import PasswordMatchError, PasswordLengthError
import random


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
            status_code = 422
        else:
            try:
                if pw != check_pw:
                    raise PasswordMatchError
                elif len(pw) < 4:
                    raise PasswordLengthError
                else:
                    user = Users(
                        username=user_id,
                        password=PasswordHasher().hash(pw),
                        hint=hint,
                        user_auth="MEMBER")
                    user.save()
                    login(request, user)
                    msg = '성공'
                    status_code = 200

            except PasswordMatchError as e:
                msg = e
                status_code = 422
            except PasswordLengthError as e:
                msg = e
                status_code = 422
            except Exception as e:
                # print(e)
                msg = '예기치 않은 오류가 발생하였습니다.'
                status_code = 500

        return msg, status_code


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
        status_code = 422
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
                status_code = 200

        return msg, status_code


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
        random_number = random.randrange(1000, 10000)
        try:
            user = Users.objects.get(username=user_id)
        except Users.DoesNotExist:
            pass
        else:
            if user.hint != hint:
                pass
            else:
                user.password = PasswordHasher().hash(str(random_number))
                user.save()
                msg = '성공'

        return msg, random_number


class MemoForm(forms.Form):
    title = forms.CharField(
        max_length=100, required=True,
        widget=forms.TextInput(attrs={
            "id": "title", "class": "form-control",
            "placeholder": "제목을 입력하여 주세요",
            "autofocus": "autofocus", "minlength": 5,
            'style': 'height:60px;font-size:18px'}))

    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "class": "form-control", "aria-label": "With textarea",
            "placeholder": "내용을 작성하여 주세요", "cols": "5", "rows": "15"}))

    img = forms.FileField(
        required=True,
        widget=forms.FileInput(attrs={
            "id": "checker", "class": "form-control"}))

    labels = forms.ChoiceField(
        widget=forms.Select(attrs={
            "id": "checker"
        })
    )
