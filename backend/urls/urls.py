from django.urls import path, include
from backend.views.account.user.views import *

urlpatterns = [
    path("auth/", include("backend.urls.account.user.urls"))
]
