import factory

# from core.models import (
#     Recruiter,
#     OpenJobs,
#     BDCity,
#     JobSource,
#     JobType,
#     JobCategory,
#     JobStatus,
# )
from common.choices import BDCity, Profession, JobCategory, JobType
from common.utils import generate_skills, generate_experiences

from core.tests import UserFactory

from recruitment.choices import JobSource, JobStatus
from recruitment.models import Recruiter, OpenJobs


class RecruiterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recruiter

    user = factory.SubFactory(UserFactory)
    company = factory.Faker("company")
    location = factory.Faker("random_element", elements=BDCity.values)


class OpenJobsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OpenJobs

    title = factory.Faker("job")
    recruiter = factory.SubFactory(RecruiterFactory)
    internal_reference = factory.Faker("word")
    job_source = factory.Faker("random_element", elements=JobSource.values)
    link = factory.Faker("url")
    profession = factory.Faker("random_element", elements=Profession.values)
    raw_job = factory.Faker("text")
    experience_year = factory.Faker("pyint", min_value=0, max_value=20)
    required_skills = generate_skills()
    required_experiences = generate_experiences()
    job_location = factory.Faker("random_element", elements=BDCity.values)
    job_type = factory.Faker("random_element", elements=JobType.values)
    job_category = factory.Faker("random_element", elements=JobCategory.values)
    job_status = factory.Faker("random_element", elements=JobStatus.values)
    attachement = factory.Faker("file_path", extension="pdf", category="document")
