"""Base URLs Mappings for candidate app."""

from django.urls import path, include


urlpatterns = [
    path("/profiles", include("candidate.rest.urls.profiles"), name="candidate-profiles"),
]