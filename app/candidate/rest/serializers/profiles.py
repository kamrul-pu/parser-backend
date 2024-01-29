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
            "recruitment_status",
            "profession_desires",
            "skills",
            "score",
            "desired_job_category",
            "job_type",
        )
        read_only_fields = ("id",)


class ProfileListSerializer(ProfileBaseSerializer):
    class Meta(ProfileBaseSerializer.Meta):
        fields = ProfileBaseSerializer.Meta.fields + (
            "original_cv",
            "experiences",
            "experience_year",
            "github_url",
            "linkedin_url",
        )
        read_only_fields = ProfileBaseSerializer.Meta.read_only_fields + ()


class ProfileDetailSerializer(ProfileBaseSerializer):
    class Meta(ProfileBaseSerializer.Meta):
        fields = ProfileBaseSerializer.Meta.fields + (
            "experiences",
            "experience_year",
            "profile_state",
            "github_url",
            "linkedin_url",
        )
        read_only_fields = ProfileBaseSerializer.Meta.read_only_fields + ()
