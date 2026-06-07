# CHeck Resume Sections
# Purpose: Check if the resume contains the required sections (Education, Experience, Skills, etc.)

def check_sections(text):

    sections = [
    "education",
    "experience",
    "projects",
    "skills",
    "certifications",
    "linkedin",
    "github",
    "summary",
    "achievements",
    "internship"
]

    missing = []

    text = text.lower()

    for section in sections:

        if section not in text:
            missing.append(section)

    return missing