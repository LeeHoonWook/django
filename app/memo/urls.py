from app.memo.views import memo_list, memo_create
from django.urls import path

urlpatterns = [
    path("list", memo_list, name="m-list"),
    path("write", memo_create, name="m-write"),

]
