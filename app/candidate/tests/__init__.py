import factory

from core.choices import UserGender
from core.tests import UserFactory

from common.choices import (
    BDCity,
    Profession,
    JobCategory,
    JobType,
)
from common.utils import generate_skills, generate_experiences

from candidate.choices import RecruitmentStatus, MaritalStatus
from candidate.models import Profile


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    city = factory.Faker("random_element", elements=BDCity.values)
    address = factory.Faker("address")
    sex = factory.Faker("random_element", elements=UserGender.values)
    dob = factory.Faker("date_of_birth")
    marital_status = factory.Faker(
        "random_element",
        elements=MaritalStatus.values,
    )
    telephone = factory.Faker("phone_number")
    email = factory.Faker("email")
    profession_desires = factory.Faker(
        "random_element",
        elements=Profession.values,
    )
    profile_state = factory.Faker(
        "random_element",
        elements=["ACTIVE", "INACTIVE"],
    )
    recruitment_status = factory.Faker(
        "random_element",
        elements=RecruitmentStatus.values,
    )
    github_url = factory.Faker("url")
    linkedin_url = factory.Faker("url")
    original_cv = factory.django.FileField(filename="original_cv.pdf")
    cv_raw = factory.Faker("text")
    experience_year = factory.Faker("random_int", min=0, max=20)
    experiences = generate_experiences()
    skills = generate_skills()
    score = factory.Faker("random_int", min=0, max=1000)
    desired_job_category = factory.Faker("random_element", elements=JobCategory.values)
    job_type = factory.Faker("random_element", elements=JobType.values)
