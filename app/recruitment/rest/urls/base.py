"""Base URLs mappings for recruitment."""

from django.urls import path, include


urlpatterns = [
    path(
        "/recruiter", include("recruitment.rest.urls.recruiter"), name="recuriter-urls"
    ),
    path(
        "/open-jobs",
        include("recruitment.rest.urls.open_jobs"),
        name="open-jobs-endpoints",
    ),
    path("/matches", include("recruitment.rest.urls.match")),
]
