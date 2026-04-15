import json
from utils.preprocess import preprocess_text

# -------------------------------
# 🔹 Load Job Roles & Skills
# -------------------------------
def load_job_roles(json_path="data/job_roles.json"):
    """
    Load job roles and skills from JSON file
    """
    with open(json_path, "r") as f:
        roles = json.load(f)
    return roles


# -------------------------------
# 🔹 Extract Skills from Resume
# -------------------------------
def extract_skills(resume_text, job_role, json_path="data/job_roles.json"):
    """
    Extract matched and missing skills from resume
    """
    roles = load_job_roles(json_path)

    # Preprocess resume text
    tokens = preprocess_text(resume_text)
    tokens_set = set(tokens)   # Faster lookup

    # Get skills for selected role
    role_skills = roles.get(job_role, [])

    matched_skills = []
    missing_skills = []

    for skill in role_skills:
        # Handle multi-word skills like "machine learning"
        skill_tokens = preprocess_text(skill)

        if all(word in tokens_set for word in skill_tokens):
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills


# -------------------------------
# 🔹 Get All Available Roles
# -------------------------------
def get_all_roles(json_path="data/job_roles.json"):
    """
    Return list of all job roles
    """
    roles = load_job_roles(json_path)
    return list(roles.keys())


# -------------------------------
# 🔹 Count Skill Frequency
# -------------------------------
def skill_frequency(tokens):
    """
    Count frequency of words in resume
    """
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq