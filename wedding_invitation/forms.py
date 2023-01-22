from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        if kwargs.get("guest"):
            guest = kwargs.pop("guest")
        else:
            guest = ""
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # 全てのフォームの部品にplaceholderを定義して、入力フォームにフォーム名が表示されるように指定する
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label
        self.fields["username"].initial = guest


class Invitation(forms.Form):
    participation = forms.ChoiceField(
        choices=(("attendance", "ご出席"), ("absence", "ご欠席")),
        widget=forms.widgets.RadioSelect(attrs={"required": True}),
        required=True,
    )
    questionnaire = forms.CharField(
        label="アレルギー等に関するご質問",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "style": "width: 90%; margin: 0 auto;"}),
    )
