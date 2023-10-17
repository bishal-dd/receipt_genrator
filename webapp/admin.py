from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.models import User
from .models import Version
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'version', 'change_mode')

    def version(self, obj):
        try:
            version = Version.objects.get(user=obj)
            return format_html(version.toggle_button)
        except Version.DoesNotExist:
            return "N/A"

    version.short_description = "version"

    def change_mode(self, obj):
        return format_html('<a class="btn" href="{}">Change Mode</a>',
                           reverse('webapp:change_mode', args=[obj.id]))

    change_mode.short_description = "Change Mode"

    actions = [change_mode]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


