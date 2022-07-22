from app.memo.views import memo_list, memo_create, memo_view, memo_update
from django.urls import path

urlpatterns = [
    path("list", memo_list, name="m-list"),
    path("write", memo_create, name="m-write"),
    path("view/<int:memo_id>", memo_view, name="m-view"),
    path("rewrite/<int:memo_id>", memo_update, name="m-rewrite")

]
