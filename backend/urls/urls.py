from django.urls import path, include
from backend.views.user.user.views import *

urlpatterns = [
    path("auth/", include("backend.urls.user.account.urls"))
]
