from django.urls import path, include, re_path
from backend.views.user.account.views import *

urlpatterns = [
    path("auth/", include("backend.urls.user.account.urls")),
    re_path("getinfo/", getinfo),
]
