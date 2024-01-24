"""Test for user endpoints."""

import json

from django.contrib.auth import get_user_model

from rest_framework import status

from core.tests import UserFactory

from common.base_test import BaseTest
from common.url_helpers import get_url_by_name, get_detail_url_by_name_id

from .payloads import get_admin_user_payload


class UserApiTest(BaseTest):
    """User Endpoints Tests."""

    url = get_url_by_name("user-list")

    def test_user_list(self):
        # Check unauthorized access when not logged in
        self.client.logout()
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Check successful access for admin user
        # Set token for user
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + self.user_login.data["access"],
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 1)

    def test_create_user(self):
        # Check that admin user can create a new user
        payload = get_admin_user_payload()

        response = self.client.post(
            path=self.url, data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the response contains the correct user data
        response_data = response.json()
        self.assertEqual(response_data["email"], payload["email"])
        # Check that UID is available in the response
        self.assertIn("uid", response_data)

    def test_user_detail(self):
        # Create a user using the UserFactory
        user = UserFactory()
        url = get_detail_url_by_name_id(name="user-details", id=user.id)

        # Check successful retrieval of user details
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(user.first_name, response_data["first_name"])

        # Test updating user first name
        payload = {
            "first_name": "Shakil",
            "last_name": "Ahmed",
        }
        response = self.client.patch(
            path=url, data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Get the user's updated data from the database
        user.refresh_from_db()
        self.assertEqual(user.first_name, payload["first_name"])
        self.assertEqual(user.last_name, payload["last_name"])

    def test_delete_user_success(self):
        # Create a user using the UserFactory
        user = UserFactory()
        url = get_detail_url_by_name_id(name="user-details", id=user.id)

        # Check successful deletion of a user
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # check it is doesn't exists in database
        user_db = get_user_model().objects.filter(id=user.id)

        self.assertEqual(len(user_db), 0)
