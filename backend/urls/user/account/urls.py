from django.urls import path, re_path
from backend.views.user.user.views import *

urlpatterns = [
    path("register/", register, name="user_register"),
    re_path("login/", login),
]
