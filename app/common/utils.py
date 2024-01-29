"""Common util methods."""

import random


experience_levels: list[str] = ["Beginner", "Intermediate", "Advanced", "Expert"]

programming_languages: list[str] = [
    "Python",
    "JavaScript",
    "Java",
    "C",
    "C#",
    "C++",
    "Ruby",
    "Swift",
    "Kotlin",
    "TypeScript",
    "PHP",
    "Go",
    "Rust",
    "Dart",
    "Objective-C",
    "R",
    "Shell",
    "MATLAB",
    "Scala",
    "Groovy",
    "HTML",
    "CSS",
    # Add more languages as needed
]

frameworks: list[str] = [
    "Django",
    "DRF",
    "Flask",
    "FastAPI",
    "Pyramid",
    "CherryPy",
    "Tornado",
    "Bottle",
    "Dash",
    "Streamlit",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Keras",
    "Flask-RESTful",
    "Django REST framework",
    "FastAPI",
    "Vue.js",
    "React",
    "Angular",
    "Express.js",
    "Spring Boot",
    "Ruby on Rails",
    "Laravel",
    "Symfony",
    "ASP.NET Core",
]


def generate_skills() -> dict:
    selected_languages = random.sample(programming_languages, random.randint(3, 4))
    selected_frameworks = random.sample(frameworks, random.randint(3, 4))

    return {
        "programming_languages": selected_languages,
        "frameworks": selected_frameworks,
    }


def generate_experiences() -> dict:
    language_experience = {
        lang: random.choice(experience_levels)
        for lang in random.sample(programming_languages, random.randint(3, 4))
    }
    framework_experience = {
        framework: random.choice(experience_levels)
        for framework in random.sample(frameworks, random.randint(3, 4))
    }

    return {
        "programming_languages": language_experience,
        "frameworks": framework_experience,
    }


# # from twilio.rest import Client
# from django.conf import settings


# def generate_unique_otp(length=6) -> str:
#     otp = "".join(random.choices("0123456789", k=length))

#     return otp


# def send_sms(phone_number: str, message: str):
#     # Twilio client with account SID and auth token

#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

#     if phone_number.startswith("0"):
#         phone_number = "+88" + phone_number

#     message = client.messages.create(
#         to=phone_number, from_=settings.TWILIO_PHONE_NUMBER, body=message
#     )
