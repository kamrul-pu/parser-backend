"""Payloads for core app."""


def get_superuser_create_payload():
    return {
        "first_name": "Kamrul",
        "last_name": "Hasan",
        "email": "kamrul@example.com",
        "password": "testpass123",
    }


def get_admin_user_payload()->dict:
    return {
            "email": "test1@example.com",
            "first_name": "Md.",
            "last_name": "Ali",
            "gender": "MALE",
            "kind": "ADMIN",
        }
