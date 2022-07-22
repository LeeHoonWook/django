from app.label.views import label_list, label_create
from django.urls import path

urlpatterns = [
    path("list", label_list, name="l-list"),
    path("write", label_create, name="l-write"),

]
