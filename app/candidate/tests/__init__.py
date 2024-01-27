import factory
import random
import time

from core.tests import UserFactory
from candidate.choices import MaritalStatus, RecruitmentStatus
from candidate.models import Profile


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    city = factory.Faker("city")
    address = factory.Faker("address")
    sex = factory.Faker("random_element", elements=["Male", "Female", "Other"])
    dob = factory.Faker("date_of_birth")
    marital_status = factory.Faker(
        "random_element", elements=["Single", "Married", "Other"]
    )
    telephone = factory.Faker("phone_number")
    email = factory.Faker("email")
    profession_desires = factory.Faker("job")
    profile_state = factory.Faker("random_element", elements=["Active", "Inactive"])
    recruitment_status = factory.Faker(
        "random_element", elements=["Pending", "Approved", "Rejected"]
    )
    github_url = factory.Faker("url")
    linkedin_url = factory.Faker("url")
    original_cv = factory.django.FileField(filename="original_cv.pdf")
    cv_raw = factory.Faker("text")
    # skills = factory.Faker("pydict")
    commercial_level = factory.Faker(
        "random_element", elements=["High", "Medium", "Low"]
    )
    score = factory.Faker("random_int", min=0, max=1000)
    # job_request = factory.Faker("pydict")
