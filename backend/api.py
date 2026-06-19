from fastapi import FastAPI
from backend.ats_score import calculate_ats_score

app = FastAPI(
    title="ResumeAI-Pro API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "ResumeAI-Pro Backend Running"
    }


@app.get("/analyze")
def analyze():

    result = calculate_ats_score(
        "resumes/sample_resume.pdf",
        "jd/sample_jd.txt"
    )

    return result