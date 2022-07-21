"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index
from django.conf.urls import include

# rest_framework
from rest_framework import routers
from app.memo.apis import *

# 이미지
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'memos', MemoViewSet)
router.register(r'labels', LabelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),

    path("user/", include("app.user.urls")),
    path("memo/", include("app.memo.urls")),

    # rest_framework
    path("apis/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )
