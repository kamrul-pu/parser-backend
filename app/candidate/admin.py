"""Admin panel configuration for candidate app."""

from django.contrib import admin

from candidate.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "recruitment_status", "score",)


admin.site.register(Profile, ProfileAdmin)