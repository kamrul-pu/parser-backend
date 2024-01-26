"""URLs mapping for open job related endpoints."""

from django.urls import path

from recruitment.rest.views.open_jobs import OpenJobList, OpenJobDetail


urlpatterns = [
    path("", OpenJobList.as_view(), name="open-jobs-list"),
    path("/<int:pk>", OpenJobDetail.as_view(), name="open-job-detail"),
]
