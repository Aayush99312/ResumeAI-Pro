import pandas as pd


def extract_skills(text, skills_file="dataset/skills.csv"):
    """
    Extract skills from resume text.
    """

    skills_df = pd.read_csv(skills_file, header=None)

    skills = skills_df[0].tolist()

    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


# Test

if __name__ == "__main__":

    sample = """
    I know Python, SQL, Machine Learning,
    Docker and AWS.
    """

    detected = extract_skills(sample)

    print("\nDetected Skills:\n")

    for skill in detected:
        print(skill)