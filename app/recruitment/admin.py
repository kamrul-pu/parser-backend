"""
Register recruitment related models here.
"""

from django.contrib import admin


from recruitment.models import Recruiter, OpenJobs, Match


class RecruiterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "status",
        "location",
        "company",
    )


admin.site.register(Recruiter, RecruiterAdmin)


class OpenJobsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "title",
        "profession",
        "job_location",
        "job_type",
        "job_category",
        "job_status",
    )


admin.site.register(OpenJobs, OpenJobsAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "recruitment_status",
        "status",
    )


admin.site.register(Match, MatchAdmin)
