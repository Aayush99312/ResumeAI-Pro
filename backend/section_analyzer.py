def analyze_resume_sections(text):
    """
    Detect important resume sections.
    """

    sections = {

        "Summary": [
            "summary",
            "profile",
            "objective"
        ],

        "Education": [
            "education",
            "qualification"
        ],

        "Skills": [
            "skills",
            "technical skills"
        ],

        "Projects": [
            "projects",
            "project"
        ],

        "Experience": [
            "experience",
            "work experience"
        ],

        "Certifications": [
            "certifications",
            "certificate"
        ],

        "Achievements": [
            "achievements",
            "awards"
        ]
    }

    text = text.lower()

    result = {}

    for section, keywords in sections.items():

        found = any(
            keyword in text
            for keyword in keywords
        )

        result[section] = found

    return result


# Test

if __name__ == "__main__":

    sample = """

    SUMMARY

    EDUCATION

    SKILLS

    PROJECTS

    """

    output = analyze_resume_sections(sample)

    print()

    print("Resume Sections")

    print("----------------")

    for key, value in output.items():

        if value:

            print(f"✅ {key}")

        else:

            print(f"❌ {key}")