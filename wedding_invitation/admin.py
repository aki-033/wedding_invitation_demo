from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, FamilyUser


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {"fields": ("guest_name", "honorific_title", "participation", "questionnaire", "message")},
        ),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # 管理サイトから追加するときのフォーム
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "guest_name"),
            },
        ),
    )

    list_display = ("username", "guest_name", "honorific_title", "participation", "is_staff")
    search_fields = ("username", "guest_name")


admin.site.register(User, CustomUserAdmin)
admin.site.register(FamilyUser)
