from django.contrib import admin

from users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'invite_code',
        'used_invite_code',
        'invited_by',
    )