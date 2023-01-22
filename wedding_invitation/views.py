from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from .forms import LoginForm, Invitation

from .models import User


def index(request):

    context = {"guest": request.user}

    return render(request, "wedding_invitation/index.html", context)


class Login(LoginView):
    template_name = "wedding_invitation/login.html"
    form_class = LoginForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if self.request.method == "GET":
            try:
                guest = self.request.GET["guest"]
            except:
                raise Http404("ページがありません。")

            kwargs.update({"guest": guest})
        return kwargs


def invitation(request):

    family_users = request.user.familyuser_set.order_by("display_order").all()

    form = Invitation()

    if request.method == "GET":
        pass
    else:
        form_result = Invitation(request.POST)
        if form_result.is_valid():
            participation = form_result.cleaned_data.get("participation")
            questionnaire = form_result.cleaned_data.get("questionnaire")

            user_obj = request.user
            user_obj.participation = True if participation == "attendance" else False
            user_obj.questionnaire = questionnaire
            user_obj.save()

    context = {
        "guest": request.user,
        "family_users": family_users,
        "form": form,
        "message": request.user.message,
        "participation": request.user.participation,
    }

    return render(request, "wedding_invitation/invitation.html", context)
