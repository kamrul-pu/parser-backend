from django.db.models import TextChoices


class UserKind(TextChoices):
    ADMIN = "ADMIN", "Admin"
    CANDIDATE = "CANDIDATE", "Candidate"
    DEVELOPER = "DEVELOPER", "Developer"
    RECRUITER = "RECRUITER", "Recruiter"
    SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
    UNDEFINED = "UNDEFINED", "Undefined"


class UserGender(TextChoices):
    FEMALE = "FEMALE", "Female"
    MALE = "MALE", "Male"
    UNKNOWN = "UNKNOWN", "Unknown"
    OTHER = "OTHER", "Other"
