"""Models for Candidates."""

from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.db import models

from common.choices import BDCity, Profession, JobCategory, JobType
from common.models import BaseModelWithUID
from core.choices import UserGender
from candidate.choices import RecruitmentStatus, MaritalStatus

User = get_user_model()


class Profile(BaseModelWithUID):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_profile",
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        db_index=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        db_index=True,
    )
    city = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
        choices=BDCity.choices,
        default=BDCity.UNKNOWN,
    )
    address = models.TextField(
        blank=True,
        null=True,
    )
    sex = models.CharField(
        blank=True,
        choices=UserGender.choices,
        default=UserGender.UNKNOWN,
        max_length=20,
    )
    dob = models.DateField(
        blank=True,
        null=True,
    )
    marital_status = models.CharField(
        max_length=100,
        blank=True,
        choices=MaritalStatus.choices,
        default=MaritalStatus.OTHER,
    )
    telephone = models.CharField(
        max_length=20,
        blank=True,
        db_index=True,
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
    )
    profession_desires = models.CharField(
        max_length=255,
        choices=Profession.choices,
        default=Profession.OTHER,
    )
    profile_state = models.CharField(
        max_length=100,
        blank=True,
    )
    recruitment_status = models.CharField(
        max_length=100,
        blank=True,
        choices=RecruitmentStatus.choices,
        default=RecruitmentStatus.PENDING,
    )
    github_url = models.URLField(
        blank=True,
    )
    linkedin_url = models.URLField(
        blank=True,
    )
    # The cv users upload will store here
    original_cv = models.FileField(
        blank=True,
        null=True,
        upload_to="original_cvs",
    )
    # extracted text from cv will be store here
    cv_raw = models.TextField(
        blank=True,
        null=True,
    )
    skills = models.JSONField(
        default=dict,
        blank=True,
    )
    experiences = models.JSONField(
        default=dict,
        blank=True,
    )
    experience_year = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(20)],
    )
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        default=0,
    )
    desired_job_category = models.CharField(
        max_length=30,
        choices=JobCategory.choices,
        default=JobCategory.ANY,
    )
    job_type = models.CharField(
        max_length=30,
        choices=JobType.choices,
        default=JobType.OTHER,
    )
    # jrsp = models.JSONField(
    #     default=dict,
    #     blank=True,
    # )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.city}"

    class Meta:
        verbose_name_plural = "Profiles"
