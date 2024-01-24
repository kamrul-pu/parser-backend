"""Serializers for candidate profiles."""

from rest_framework import serializers

from candidate.models import Profile


class ProfileBaseSerializer(serializers.ModelSerializer):
    """Profile Base serializer"""

    class Meta:
        model = Profile
        fields = (
            "id",
            "first_name",
            "last_name",
            "city",
            "sex",
            "dob",
            "marital_status",
            "telephone",
            "email",
            "profession_desires",
            "profile_state",
            "recruitment_status",
            "cv_raw",
            "skills",
            "commercial_level",
            "score",
        )
        read_only_fields = ("id",)


class ProfileListSerializer(ProfileBaseSerializer):
    class Meta(ProfileBaseSerializer.Meta):
        fields = ProfileBaseSerializer.Meta.fields + ("job_request",)
        read_only_fields = ProfileBaseSerializer.Meta.read_only_fields + ()


class ProfileDetailSerializer(ProfileBaseSerializer):
    class Meta(ProfileBaseSerializer.Meta):
        fields = ProfileBaseSerializer.Meta.fields + ("job_request",)
        read_only_fields = ProfileBaseSerializer.Meta.read_only_fields + ()