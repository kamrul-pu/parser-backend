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
        "desired_profession": "Hydrologist",
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
        "commercial_level": "Not Yet",
        "score": 27,
        "job_request": {
            "occupation": "Python Developer",
            "salary": 70000,
            "nationality": "France",
            "date_posted": "2023-02-15",
            "city": "Toulouse",
            "country": "France",
            "start_date": "2023-03-15",
            "urgency": "Urgent",
            "age": 30,
            "years_of_experience": 7,
            "skills": {
                "occupational": ["Python", "Django", "Flask", "RESTful API", "SQL"],
                "human": ["Team Spirit", "Problem Solving"],
                "functional": ["Analysis", "Design"],
            },
            "professional_experience": [
                "Web Application Development",
                "Database Management",
            ],
            "education_level": "Master's",
            "telecommute_mobility": "Possible Telecommute",
            "preferred_activity_sectors": ["Information Technology", "Startup"],
            "security_clearance": "Yes",
            "defense": "No",
            "certifications": ["Certified Python", "Certified SQL"],
            "extras": "Passionate about new technologies",
        },
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
