def generate_suggestions(
    ats_score,
    missing_skills,
    semantic_score
):
    """
    Generates AI-like suggestions based on ATS score,
    semantic similarity and missing skills.
    """

    suggestions = []

    # ATS based suggestions
    if ats_score < 50:
        suggestions.append(
            "Overall resume needs significant improvement for ATS systems."
        )

    elif ats_score < 70:
        suggestions.append(
            "Resume is moderately optimized but can be improved."
        )

    else:
        suggestions.append(
            "Resume is well optimized for ATS screening."
        )

    # Semantic Similarity
    if semantic_score < 60:
        suggestions.append(
            "Tailor your resume more closely to the target job description."
        )

    # Missing Skills
    for skill in missing_skills:
        suggestions.append(
            f"Consider adding experience or projects related to '{skill}'."
        )

    # Generic suggestions
    suggestions.append(
        "Use quantified achievements wherever possible."
    )

    suggestions.append(
        "Keep project descriptions impact-oriented."
    )

    suggestions.append(
        "Include GitHub and LinkedIn profile links."
    )

    return suggestions


# Test

if __name__ == "__main__":

    ats = 52

    semantic = 45

    missing = [
        "Docker",
        "AWS",
        "TensorFlow"
    ]

    result = generate_suggestions(
        ats,
        missing,
        semantic
    )

    print("\nAI Suggestions\n")

    for s in result:
        print("•", s)