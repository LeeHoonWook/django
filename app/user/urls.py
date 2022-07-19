from app.user.views import login_view, register, logout_view, user_check, user_find
from django.urls import path

urlpatterns = [
    path("login", login_view, name="login"),
    path("register", register, name="register"),
    path("logout", logout_view, name="logout"),

    path("check", user_check, name="user_check"),
    path("find", user_find, name="user_find"),
]
