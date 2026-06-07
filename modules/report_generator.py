# modules/report_generator.py

def generate_report(
        ats_score,
        similarity_score,
        matched_skills,
        missing_skills,
        missing_sections,
        suggestions
):

    report = f"""
===================================
AI RESUME ANALYZER REPORT
===================================

ATS Score: {ats_score}%

Match Score: {similarity_score}%

Matched Skills:
{", ".join(matched_skills)}

Missing Skills:
{", ".join(missing_skills)}

Missing Sections:
{", ".join(missing_sections)}

Suggestions:
"""

    for suggestion in suggestions:
        report += f"\n• {suggestion}"

    return report