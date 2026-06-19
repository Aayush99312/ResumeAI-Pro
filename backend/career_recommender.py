def recommend_roles(skills):
    """
    Recommends career roles based on extracted skills.
    """

    role_database = {

        "Machine Learning Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch"
        ],

        "Data Scientist": [
            "Python",
            "SQL",
            "Machine Learning",
            "Pandas",
            "NumPy"
        ],

        "AI Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "TensorFlow"
        ],

        "Backend Developer": [
            "Python",
            "SQL",
            "Flask",
            "Django",
            "API"
        ],

        "Full Stack Developer": [
            "React",
            "Node.js",
            "MongoDB",
            "JavaScript",
            "HTML",
            "CSS"
        ]
    }

    recommendations = []

    user_skills = set(skill.lower() for skill in skills)

    for role, required in role_database.items():

        required_set = set(skill.lower() for skill in required)

        matched = len(user_skills & required_set)

        score = round(
            (matched / len(required_set)) * 100,
            2
        )

        recommendations.append(
            (role, score)
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations


# Test

if __name__ == "__main__":

    resume_skills = [

        "Python",

        "SQL",

        "Machine Learning",

        "TensorFlow",

        "Pandas"

    ]

    result = recommend_roles(
        resume_skills
    )

    print("\nRecommended Roles\n")

    for role, score in result:

        print(role, "-", score, "%")