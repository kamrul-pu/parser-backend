"""Utils functions for Recruitment apps."""

from typing import List, Dict

from fuzzywuzzy import fuzz

from candidate.models import Profile

from recruitment.models import OpenJobs, Match


def lcs(s1: str, s2: str) -> int:
    """
    Function to find the length of the Longest Common Subsequence (LCS)
    using an optimized space (rolling array) dynamic programming approach.

    Args:
        s1 (str): First input string.
        s2 (str): Second input string.

    Returns:
        int: Length of LCS for the input strings.
    """
    n: int = len(s1)
    m: int = len(s2)
    prev: List[int] = [0 for col in range(m + 1)]
    cur: List[int] = [0 for col in range(m + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the current characters match, increment the LCS length.
            if s1[i - 1] == s2[j - 1]:
                cur[j] = 1 + prev[j - 1]
            else:
                # If the current characters don't match, choose the maximum LCS
                # from excluding one character from either of the strings.
                cur[j] = max(prev[j], cur[j - 1])

        # Update the previous array for the next iteration.
        prev = cur.copy()

    return prev[m]


def get_experiences_score(
    required_experiences: Dict, candidate_experiences: Dict
) -> int:
    """
    Calculate the score based on matching required experiences with candidate experiences.

    Args:
        required_experiences (Dict): Dictionary of required experiences.
        candidate_experiences (Dict): Dictionary of candidate experiences.

    Returns:
        int: Experience score.
    """
    experience_score: int = 0
    # Iterate over keys in required experiences
    for key in required_experiences.keys():
        # Convert required and candidate experiences to lowercase strings
        required_experience = " ".join(
            map(str, required_experiences.get(key, []))
        ).lower()
        candidate_experience = " ".join(
            map(str, candidate_experiences.get(key, []))
        ).lower()
        # Calculate partial ratio score and add to experience_score
        experience_score += fuzz.partial_ratio(
            required_experience, candidate_experience
        )
    return experience_score


def get_skills_score(required_skills, candidate_skills):
    """
    Calculate the score based on matching required skills with candidate skills.

    Args:
        required_skills (Dict): Dictionary of required skills.
        candidate_skills (Dict): Dictionary of candidate skills.

    Returns:
        int: Skill score.
    """
    skill_score: int = 0
    # Iterate over keys in required skills
    for key in required_skills.keys():
        # Convert required and candidate skills to lowercase strings
        skills = ", ".join(map(str, required_skills.get(key, []))).lower()
        candidate_skill = ", ".join(map(str, candidate_skills.get(key, []))).lower()
        # Calculate partial ratio score and add to skill_score
        skill_score += fuzz.partial_ratio(skills, candidate_skill)
    return skill_score


def calculate_profile_score(profile: Profile, job: OpenJobs) -> int:
    """
    Calculate the profile score based on experience years, required skills, and required experiences.

    Args:
        profile (Profile): Profile object.
        job (OpenJobs): OpenJobs object.

    Returns:
        int: Profile score.
    """
    score: int = 0
    # Add experience years to score
    score += profile.experience_year
    # Add skills score to score
    score += get_skills_score(job.required_skills, profile.skills)
    # Add experiences score to score
    score += get_experiences_score(job.required_experiences, profile.experiences)

    return score


def generate_job_matched_profile(job_id: int) -> Match:
    """
    Generate matched profiles for a given job ID.

    Args:
        job_id (int): ID of the job.

    Returns:
        Object: created or updated match.
    """
    # Retrieve job object by ID
    job = OpenJobs.objects.get(id=job_id)
    # Retrieve active profiles matching the job's profession and excluding profiles without skills
    profiles = (
        Profile()
        .get_all_actives()
        .filter(profession_desires__iexact=job.profession)
        .exclude(skills={})
    )

    # Initialize dictionaries for same and different city matches
    same_city_matches = dict()
    different_city_matches = dict()

    # Iterate over profiles to calculate scores and categorize matches
    for profile in profiles:
        score: int = calculate_profile_score(profile, job)
        if profile.city == job.job_location:
            same_city_matches[profile.id] = score
        else:
            different_city_matches[profile.id] = score

    # Retrieve existing match object if available, otherwise create a new one
    matches = Match().get_all_actives().filter(open_job_id=job.id).first()
    if matches:
        # Update existing match
        matches.same_city_matches = same_city_matches
        matches.different_city_matches = different_city_matches
        matches.save(update_fields=["same_city_matches", "different_city_matches"])
    else:
        # Create new match
        matches = Match.objects.create(
            open_job_id=job_id,
            same_city_matches=same_city_matches,
            different_city_matches=different_city_matches,
        )

    return matches
