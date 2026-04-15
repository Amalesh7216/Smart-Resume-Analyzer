# -------------------------------
# 🔹 Calculate Resume Score
# -------------------------------
def calculate_score(matched_skills, total_skills):
    """
    Calculate score based on matched skills
    Formula:
    (matched / total) * 100
    """
    if total_skills == 0:
        return 0

    score = (len(matched_skills) / total_skills) * 100
    return round(score, 2)


# -------------------------------
# 🔹 Detailed Score Breakdown
# -------------------------------
def score_details(matched_skills, missing_skills):
    """
    Provide detailed breakdown of score
    """
    total = len(matched_skills) + len(missing_skills)

    score = calculate_score(matched_skills, total)

    return {
        "score": score,
        "matched_count": len(matched_skills),
        "missing_count": len(missing_skills),
        "total_skills": total
    }


# -------------------------------
# 🔹 Resume Rating (Grade)
# -------------------------------
def get_resume_rating(score):
    """
    Convert score into rating
    """
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
    else:
        return "Needs Improvement"


# -------------------------------
# 🔹 ATS Compatibility Level
# -------------------------------
def ats_level(score):
    """
    Simulate ATS compatibility
    """
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"