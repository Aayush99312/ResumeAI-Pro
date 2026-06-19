from parser import extract_text
from preprocess import preprocess_text
from skill_extractor import extract_skills
from jd_parser import parse_job_description


def compare_resume_jd(resume_path, jd_path):

    # Resume
    resume_text = extract_text(resume_path)
    cleaned_resume = preprocess_text(resume_text)
    resume_skills = extract_skills(cleaned_resume)

    # JD
    _, _, jd_skills = parse_job_description(jd_path)

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = sorted(list(resume_set & jd_set))
    missing = sorted(list(jd_set - resume_set))

    match_percentage = round(
        (len(matched) / len(jd_set)) * 100, 2
    )

    return matched, missing, match_percentage


if __name__ == "__main__":

    matched, missing, score = compare_resume_jd(
        "resumes/sample_resume.pdf",
        "jd/sample_jd.txt"
    )

    print("\nMatched Skills:\n")
    for skill in matched:
        print(skill)

    print("\nMissing Skills:\n")
    for skill in missing:
        print(skill)

    print("\nSkill Match Score:", score, "%")