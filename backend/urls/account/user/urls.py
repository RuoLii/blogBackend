from django.urls import path
from backend.views.account.user.views import *

urlpatterns = [
    path("register/", register, name="user_register")
]
