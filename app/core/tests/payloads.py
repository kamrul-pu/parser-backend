"""Payloads for core app."""


def superuser_create_payload():
    return {
        "first_name": "Kamrul",
        "last_name": "Hasan",
        "email": "kamrul@example.com",
        "password": "testpass123",
    }
