"""Models for recruitement related data."""

from django.db import models

from autoslug import AutoSlugField

from common.choices import BDCity
from common.models import BaseModelWithUID

from recruitment.choices import JobStatus, JobSource, JobType


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
    city = models.CharField(
        max_length=255,
        choices=BDCity.choices,
        default=BDCity.UNKNOWN,
        db_index=True,
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
    job_requirements = models.JSONField(
        default=dict,
        blank=True,
    )
    job_location = models.CharField(
        max_length=255,
        blank=True,
    )
    job_type = models.CharField(
        max_length=30,
        choices=JobType.choices,
        default=JobType.OTHER,
    )
    job_status = models.CharField(
        max_length=30,
        choices=JobStatus.choices,
        default=JobStatus.DRAFT,
    )
    files = models.FileField(
        upload_to="job-files",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.city}"

    class Meta:
        verbose_name_plural = "Open Jobs"
