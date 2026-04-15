# -------------------------------
# 🔹 Generate Suggestions
# -------------------------------
def generate_suggestions(missing_skills, score):
    """
    Generate suggestions based on missing skills and score
    """
    suggestions = []

    # Suggest adding missing skills
    for skill in missing_skills[:5]:   # limit to top 5
        suggestions.append(f"Add '{skill}' to your resume")

    # Score-based suggestions
    if score >= 80:
        suggestions.append("Great job! Your resume is well optimized.")
    elif score >= 60:
        suggestions.append("Good resume, but adding a few more relevant skills can improve it.")
    elif score >= 40:
        suggestions.append("Your resume needs improvement. Focus on adding key skills and projects.")
    else:
        suggestions.append("Your resume is not well aligned. Consider updating skills and gaining relevant experience.")

    return suggestions


# -------------------------------
# 🔹 Suggest Resume Improvements
# -------------------------------
def resume_tips():
    """
    General resume improvement tips
    """
    tips = [
        "Use clear and professional formatting",
        "Add measurable achievements (e.g., increased accuracy by 20%)",
        "Include relevant projects",
        "Keep resume concise (1-2 pages)",
        "Use action verbs (Developed, Built, Implemented)"
    ]
    return tips


# -------------------------------
# 🔹 Suggest Missing Sections
# -------------------------------
def missing_sections(resume_text):
    """
    Check if important sections are missing
    """
    sections = {
        "education": "Add an Education section",
        "experience": "Include Work Experience",
        "projects": "Add Projects section",
        "skills": "Include Skills section",
        "certification": "Add Certifications"
    }

    suggestions = []
    text = resume_text.lower()

    for key, message in sections.items():
        if key not in text:
            suggestions.append(message)

    return suggestions