from preprocess import preprocess_text
from skill_extractor import extract_skills

def parse_job_description(jd_path):
    """
    Reads a Job Description and extracts skills.
    """

    with open(jd_path, "r", encoding="utf-8") as file:
        jd_text = file.read()

    cleaned_text = preprocess_text(jd_text)

    skills = extract_skills(cleaned_text)

    return jd_text, cleaned_text, skills


# Test

if __name__ == "__main__":

    jd_path = "jd/sample_jd.txt"

    original, cleaned, skills = parse_job_description(jd_path)

    print("\nOriginal JD:\n")
    print(original)

    print("\nCleaned JD:\n")
    print(cleaned)

    print("\nDetected Skills:\n")

    for skill in skills:
        print(skill)