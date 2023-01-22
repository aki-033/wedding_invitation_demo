from django.urls import path
from . import views

app_name = "wedding_invitation"

# fmt: off
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.Login.as_view(), name="login"),
    path("invitation/", views.invitation, name="invitation")
]
# fmt: on
