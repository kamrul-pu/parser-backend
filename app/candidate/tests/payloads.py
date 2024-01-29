"""Payloads for candidate app."""


def get_profile_payload() -> dict:
    return {
        "first_name": "Laure",
        "last_name": "Samson",
        "city": "UNKNOWN",
        "sex": "OTHER",
        "dob": "1995-02-02",
        "marital_status": "OTHER",
        "telephone": "+880198194808",
        "email": "test_1@example.com",
        "desired_profession": "ML_ENGINEER",
        "profile_state": "Validated",
        "recruitment_status": "PENDING",
        "skills": {
            "Programming Languages": [
                "Go",
                "Java",
                "Ruby",
                "JavaScript",
                "Python",
                "TypeScript",
                "Kotlin",
                "PHP",
            ],
            "Frontend": ["Next JS", "HTML", "CSS", "Vue", "Angular", "React JS."],
            "Operating System": ["Linux"],
        },
        "score": 27,
        "skills": {
            "occupational": ["Python", "Django", "Flask", "RESTful API", "SQL"],
            "human": ["Team Spirit", "Problem Solving"],
            "functional": ["Analysis", "Design"],
        },
        "experiences": [
            "Web Application Development",
            "Database Management",
        ],
    }


def get_profile_update_payload() -> dict:
    return {
        "first_name": "Laure",
        "last_name": "Samson",
        "city": "",
        "sex": "MALE",
        "skills": {
            "Frontend": ["Next JS", "HTML", "CSS", "Vue", "Angular", "React JS."],
            "Operating System": ["Linux"],
        },
    }


def get_profile_patch_payload() -> dict:
    return {
        "skills": {
            "Programming Languages": [
                "Go",
            ],
        }
    }
