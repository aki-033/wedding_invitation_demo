from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

import uuid


class User(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    # ゲスト名
    guest_name = models.CharField(verbose_name="guest_name", max_length=150, blank=True)
    # 敬称
    honorific_title = models.CharField(verbose_name="honorific_title", max_length=150, blank=True)
    # 参加/不参加
    participation = models.BooleanField(default=None, null=True)
    # 質問フォーム(アレルギー情報など)
    questionnaire = models.TextField(blank=True, null=True)
    # メッセージ
    message = models.TextField(blank=True, null=True)

    email = models.EmailField(_("email address"), blank=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["email", "handle_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        # abstract  = True         #←ここをコメントアウトしないとカスタムユーザーモデルは反映されず、マイグレーションエラーを起こす。

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        return self.guest_name

    def get_short_name(self):
        return self.guest_name

    def __str__(self):
        return self.guest_name


class FamilyUser(models.Model):
    # 代表者
    representative = models.ForeignKey(User, on_delete=models.CASCADE)

    # 表示順
    display_order = models.IntegerField()

    # ゲスト名
    guest_name = models.CharField(verbose_name="guest_name", max_length=150, blank=True)

    # 敬称
    honorific_title = models.CharField(verbose_name="honorific_title", max_length=150, blank=True)

    def __str__(self):
        return self.representative.guest_name + " - " + self.guest_name
