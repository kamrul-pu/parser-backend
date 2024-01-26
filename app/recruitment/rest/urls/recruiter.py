"""URLs for recruiter."""

from django.urls import path

from recruitment.rest.views.recruiter import RecruiterList, RecruiterDetail

urlpatterns = [
    path("", RecruiterList.as_view(), name="recruiter-list"),
    path("/<int:pk>", RecruiterDetail.as_view(), name="recruiter-detail"),
]
