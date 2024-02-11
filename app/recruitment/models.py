"""Models for recruitement related data."""

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from autoslug import AutoSlugField

from candidate.choices import RecruitmentStatus
from common.choices import BDCity, JobType, JobCategory
from common.models import BaseModelWithUID

from recruitment.choices import JobStatus, JobSource


class Recruiter(BaseModelWithUID):
    user = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="recruiter",
    )
    company = models.CharField(
        max_length=200,
        blank=True,
    )
    location = models.CharField(
        max_length=255,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.user} {self.company}"

    class Meta:
        verbose_name_plural = "Recruiters"


class OpenJobs(BaseModelWithUID):
    title = models.CharField(
        max_length=200,
    )
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
    )
    recruiter = models.ForeignKey(
        Recruiter,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="open_jobs",
    )
    internal_reference = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
        unique=True,
    )
    job_source = models.CharField(
        max_length=255,
        choices=JobSource.choices,
        default=JobSource.OTHER,
    )
    link = models.TextField(
        blank=True,
    )
    profession = models.CharField(
        max_length=255,
        blank=True,
    )
    raw_job = models.TextField(
        blank=True,
    )
    experience_year = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(20)],
    )
    required_skills = models.JSONField(
        default=dict,
        blank=True,
    )
    required_experiences = models.JSONField(
        default=dict,
        blank=True,
    )
    job_location = models.CharField(
        max_length=255,
        choices=BDCity.choices,
        default=BDCity.OTHER,
    )
    job_type = models.CharField(
        max_length=30,
        choices=JobType.choices,
        default=JobType.OTHER,
    )
    job_category = models.CharField(
        max_length=30,
        choices=JobCategory.choices,
        default=JobCategory.OTHER,
    )
    job_status = models.CharField(
        max_length=30,
        choices=JobStatus.choices,
        default=JobStatus.DRAFT,
    )
    attachement = models.FileField(
        upload_to="job-attachments",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.job_location}"

    class Meta:
        verbose_name_plural = "Open Jobs"


class Match(BaseModelWithUID):
    open_job = models.ForeignKey(
        OpenJobs,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="job_matches",
    )
    # List of profiles ids
    same_city_matches = models.JSONField(
        default=dict,
        blank=True,
        null=True,
    )
    # list of profiles ids
    different_city_matches = models.JSONField(
        default=dict,
        blank=True,
        null=True,
    )
    recruitment_status = models.CharField(
        max_length=30,
        choices=RecruitmentStatus.choices,
        default=RecruitmentStatus.PENDING,
    )

    def __str__(self) -> str:
        return f"{self.id} {self.recruitment_status}"

    class Meta:
        verbose_name_plural = "Job Match Profile"
