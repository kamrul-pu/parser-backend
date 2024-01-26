"""
Register recruitment related models here.
"""

from django.contrib import admin


from recruitment.models import Recruiter, OpenJobs


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
        "city",
        "job_type",
        "job_status",
    )


admin.site.register(OpenJobs, OpenJobsAdmin)
