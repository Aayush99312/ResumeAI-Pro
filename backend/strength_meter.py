def calculate_strength(
    ats_score,
    semantic_score,
    section_result,
    total_skills,
    matched_skills
):
    """
    Calculates Resume Strength Score.
    """

    score = 0

    # ATS Score Contribution (40)
    score += ats_score * 0.40

    # Semantic Score Contribution (30)
    score += semantic_score * 0.30

    # Section Score Contribution (20)
    total_sections = len(section_result)

    present_sections = sum(section_result.values())

    section_score = (
        present_sections / total_sections
    ) * 20

    score += section_score

    # Skill Coverage Contribution (10)

    if total_skills > 0:

        skill_score = (
            matched_skills /
            total_skills
        ) * 10

        score += skill_score

    return round(score, 2)


# ---------------- TEST ---------------- #

if __name__ == "__main__":

    ats = 68

    semantic = 74

    sections = {

        "Summary": True,

        "Education": True,

        "Skills": True,

        "Projects": True,

        "Experience": False,

        "Certifications": False,

        "Achievements": False

    }

    strength = calculate_strength(

        ats,

        semantic,

        sections,

        total_skills=10,

        matched_skills=7

    )

    print()

    print("Resume Strength")

    print("----------------")

    print(strength, "%")