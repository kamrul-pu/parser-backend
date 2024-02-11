"""Urls Mappings for match."""

from django.urls import path


from recruitment.rest.views.match import (
    MatchList,
    MatchDetail,
)

urlpatterns = [
    path("", MatchList.as_view(), name="match-list"),
    path("/<int:pk>/", MatchDetail.as_view(), name="match-detail"),
]
