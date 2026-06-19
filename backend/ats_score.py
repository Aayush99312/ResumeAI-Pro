from matcher import compare_resume_jd
from parser import extract_text
from jd_parser import parse_job_description
from similarity import calculate_similarity


def calculate_ats_score(resume_path, jd_path):
    """
    Calculates ATS Score using:
    - Skill Match (60%)
    - Semantic Similarity (40%)
    """
    

    # Skill Matching
    matched, missing, skill_score = compare_resume_jd(
        resume_path,
        jd_path
    )

    # Resume Text
    resume_text = extract_text(resume_path)

    # JD Text
    jd_text, _, _ = parse_job_description(jd_path)

    # Semantic Similarity
    semantic_score = calculate_similarity(
        resume_text,
        jd_text
    )

    # Final ATS Score
    ats_score = (
        skill_score * 0.60
        +
        semantic_score * 0.40
    )

    return {
        "ats_score": round(ats_score, 2),
        "skill_score": round(skill_score, 2),
        "semantic_score": round(semantic_score, 2),
        "matched": matched,
        "missing": missing
    }


if __name__ == "__main__":

    result = calculate_ats_score(
        "resumes/sample_resume.pdf",
        "jd/sample_jd.txt"
    )

    print("\nATS SCORE")
    print("--------------------")

    print("Overall ATS:", result["ats_score"], "%")

    print("\nSkill Score:",
          result["skill_score"], "%")

    print("\nSemantic Score:",
          result["semantic_score"], "%")

    print("\nMatched Skills:")

    for skill in result["matched"]:
        print(skill)

    print("\nMissing Skills:")

    for skill in result["missing"]:
        print(skill)