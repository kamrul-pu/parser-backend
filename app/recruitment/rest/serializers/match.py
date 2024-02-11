"""Serializer for Match Model."""

from rest_framework import serializers

from recruitment.models import Match


class MatchBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "id",
            "uid",
            "open_job",
        )
        read_only_fields = (
            "id",
            "uid",
        )


class MatchListSerializer(MatchBaseSerializer):
    class Meta(MatchBaseSerializer.Meta):
        fields = MatchBaseSerializer.Meta.fields + (
            "same_city_matches",
            "different_city_matches",
            "recruitment_status",
        )
        read_only_fields = MatchBaseSerializer.Meta.read_only_fields + ()


class MatchDetailSerializer(MatchListSerializer):
    class Meta(MatchListSerializer.Meta):
        fields = MatchListSerializer.Meta.fields + (
            "created_at",
            "updated_at",
        )
        read_only_fields = MatchListSerializer.Meta.read_only_fields + ()
