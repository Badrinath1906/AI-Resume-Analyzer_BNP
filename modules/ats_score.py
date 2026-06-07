#Calculate ATS score based on the extracted text and job description
def calculate_ats_score(
        similarity_score,
        matched_skills,
        total_skills
):

    if total_skills == 0:
        return similarity_score

    skill_score = (
        len(matched_skills)
        /
        total_skills
    ) * 100

    ats = (
        similarity_score * 0.6
        +
        skill_score * 0.4
    )

    return round(ats, 2)