"""Serializers for recruiter."""

from rest_framework import serializers

from recruitment.models import Recruiter


class RecruiterBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = (
            "id",
            "uid",
            "company",
        )

        read_only_fields = (
            "id",
            "uid",
        )


class RecruiterListSerializer(RecruiterBaseSerializer):
    class Meta(RecruiterBaseSerializer.Meta):
        fields = RecruiterBaseSerializer.Meta.fields + ("user",)
        read_only_fields = RecruiterBaseSerializer.Meta.read_only_fields + ()


class RecruiterDetailSerializer(RecruiterBaseSerializer):
    class Meta(RecruiterBaseSerializer.Meta):
        fields = RecruiterBaseSerializer.Meta.fields + (
            "user",
            "location",
        )
        read_only_fields = RecruiterBaseSerializer.Meta.read_only_fields + ()
