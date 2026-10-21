from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("BBMS Information", {
            "fields": ("role", "phone"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("BBMS Information", {
            "fields": ("role", "phone"),
        }),
    )

    list_display = (
        "username",
        "email",
        "role",
        "is_active",
        "is_staff",
    )