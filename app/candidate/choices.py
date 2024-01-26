"""Choices for Candidates."""
from django.db.models import TextChoices


class MaritalStatus(TextChoices):
    SINGLE = "SINGLE", "Single"
    MARRIED = "MARRIED", "Married"
    DIVORCED = "DIVORCED", "DIVORCED"
    OTHER = "OTHER", "Other"


class RecruitmentStatus(TextChoices):
    PENDING = "PENDING", "Pending"
    IN_PROGRESS = "IN_PROGRESS", "In_Progress"
    COMPLETED = "COMPLETED", "Completed"
    REJECTED = "REJECTED", "Rejected"
    RECRUITED = "RECRUITED", "Recruited"
    ON_HOLD = "ON_HOLD", "On_Hold"
