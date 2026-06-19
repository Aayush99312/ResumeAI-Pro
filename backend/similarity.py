from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(resume_text, jd_text):
    """
    Calculates semantic similarity between resume and job description.
    Returns percentage similarity.
    """

    resume_embedding = model.encode([resume_text])

    jd_embedding = model.encode([jd_text])

    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0]

    return round(similarity * 100, 2)


# Test

if __name__ == "__main__":

    resume = """
    Python SQL Machine Learning Git Linux
    """

    jd = """
    Python SQL Machine Learning Docker AWS TensorFlow
    """

    score = calculate_similarity(resume, jd)

    print("\nSemantic Similarity:")
    print(score, "%")