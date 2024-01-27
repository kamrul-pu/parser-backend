"""Test for profile endpoints."""

import json

from rest_framework import status

from common.base_test import BaseTest
from common.url_helpers import get_detail_url_by_name_id, get_url_by_name

from candidate.models import Profile

from candidate.tests import payloads
from candidate.tests import ProfileFactory

# from core.rest.tests.data.profile import (
#     profile_create_data,
#     profile_patch_data,
#     profile_update_data,
# )


class ProfileApiTest(BaseTest):
    """Profile Endpoints Tests"""

    list_url: str = get_url_by_name(name="profile-list-create")

    def test_profile_list(self):
        # Check unauthorized access when not logged in
        self.client.logout()
        response = self.client.get(path=self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Create a profile using the factory
        profile = ProfileFactory()

        # Set token for user
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + self.user_login.data["access"],
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["count"], 1)

    def test_profile_create(self):
        # Create a profile using the factory
        profile = ProfileFactory()
        payload = payloads.get_profile_payload()
        response = self.client.post(
            path=self.list_url,
            data=json.dumps(payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        expected_id = profile.id + 1
        self.assertEqual(data["id"], expected_id)
        self.assertEqual(data["skills"], payload["skills"])

    def test_profile_detail(self):
        # Create a profile using the factory
        profile = ProfileFactory()
        detail_url = get_detail_url_by_name_id(name="profile-detail", id=profile.id)
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["skills"], profile.skills)

    def test_profile_update(self):
        # Create a profile using the factory
        profile = ProfileFactory()
        detail_url = get_detail_url_by_name_id(name="profile-detail", id=profile.id)
        profile_update_data = payloads.get_profile_update_payload()
        response = self.client.put(
            path=detail_url,
            data=json.dumps(profile_update_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["skills"], profile_update_data["skills"])
        profile.refresh_from_db()
        self.assertEqual(profile.skills, data["skills"])

    def test_profile_patch(self):
        # Create a profile using the factory
        profile = ProfileFactory()
        detail_url = get_detail_url_by_name_id(name="profile-detail", id=profile.id)
        profile_patch_data = payloads.get_profile_patch_payload()
        response = self.client.patch(
            path=detail_url,
            data=json.dumps(profile_patch_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["skills"], profile_patch_data["skills"])
        profile.refresh_from_db()
        self.assertEqual(profile.skills, data["skills"])

    def test_profile_delete(self):
        # Create a profile using the factory
        profile = ProfileFactory()
        detail_url = get_detail_url_by_name_id(name="profile-detail", id=profile.id)
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user_db = Profile.objects.filter(id=profile.id)
        self.assertEqual(len(user_db), 0)
