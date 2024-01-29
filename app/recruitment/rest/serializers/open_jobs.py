"""Serializers for open jobs."""

from rest_framework import serializers

from recruitment.models import OpenJobs


class OpenJobBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenJobs
        fields = (
            "id",
            "uid",
            "title",
            "slug",
            "job_location",
        )
        read_only_fields = (
            "id",
            "uid",
        )


class OpenJobListSerializer(OpenJobBaseSerializer):
    class Meta(OpenJobBaseSerializer.Meta):
        fields = OpenJobBaseSerializer.Meta.fields + (
            "recruiter",
            "internal_reference",
            "job_source",
            "link",
            "profession",
            "raw_job",
            "job_requirements",
            "job_type",
            "job_category",
            "job_status",
            "attachment",
        )
        read_only_fields = OpenJobBaseSerializer.Meta.read_only_fields + ()


class OpenJobDetailSerializer(OpenJobListSerializer):
    class Meta(OpenJobListSerializer.Meta):
        fields = OpenJobListSerializer.Meta.fields + (
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = OpenJobListSerializer.Meta.read_only_fields + ()
