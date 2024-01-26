"""Text choices for recruitement app."""

from django.db.models import TextChoices


class JobSource(TextChoices):
    BD_JOBS = "BD_JOBS", "Bd_Jobs"
    INDEED = "INDEED", "INDEED"
    INTERNAL = "INTERNAL", "Internal"
    LINKEDIN = "LINKEDIN", "Likedin"
    NEWS_PAPER = "NEWS_PAPER", "News_Paper"
    RECRUITER = "RECRUITER", "Recruiter"
    OTHER = "OTHER", "Other"


class JobStatus(TextChoices):
    CLOSED = "CLOSED", "Closed"
    DRAFT = "DRAFT", "DRAFT"
    OPEN = "OPEN", "Open"
    PUBLISHED = "PUBLISHED", "Published"
    REJECTED = "REJECTED", "Rejected"


class JobType(TextChoices):
    CONTRACTUAL = "CONTRACTUAL", "Contractual"
    FULL_TIME = "FULL_TIME", "Full_Time"
    PART_TIME = "PART_TIME", "Part_Time"
    PERMANENT = "PERMANENT", "Permanent"
    TEMPORARY = "TEMPORARY", "Temporary"
    OTHER = "OTHER", "OTHER"
