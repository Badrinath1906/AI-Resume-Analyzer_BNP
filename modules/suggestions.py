#Purpose: Analyze the resume and provide suggestions for improvement
#Check for missing sections (Education, Experience, Skills, etc.)
#Check for missing skills based on job description
#Generate improvement suggestions.
def generate_suggestions(
        missing_skills,
        missing_sections
):

    suggestions = []

    for skill in missing_skills:

        suggestions.append(
            f"""
Missing Skill: {skill}

✔ Add projects using {skill}
✔ Mention practical experience
✔ Add certification related to {skill}
"""
        )

    for section in missing_sections:

        suggestions.append(
            f"⚠ Add {section.title()} section"
        )

    if not suggestions:

        suggestions.append(
            "Excellent Resume! No major gaps found."
        )

    return suggestions