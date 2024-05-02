from django.urls import path, re_path
from backend.views.user.account.views import *

urlpatterns = [
    path("register/", register, name="user_register"),
    re_path("login/", login),
    path("updateAvatar/", updateAvatar, name="updateAvatar"),
]
