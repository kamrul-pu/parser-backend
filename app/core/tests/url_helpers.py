"""Url helpers for core app."""

from django.urls import reverse


def get_token_url(name: str) -> str:
    return reverse(name)
