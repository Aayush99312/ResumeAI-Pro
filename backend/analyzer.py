from backend.parser import extract_text
from backend.preprocess import preprocess_text
from backend.skill_extractor import extract_skills
from backend.jd_parser import parse_job_description
from backend.matcher import compare_resume_jd
from backend.similarity import calculate_similarity
from backend.ats_score import calculate_ats_score
from backend.suggestions import generate_suggestions
from backend.career_recommender import recommend_roles
from backend.section_analyzer import analyze_resume_sections
from backend.strength_meter import calculate_strength

def analyze_resume(
    resume_path,
    jd_path
):
    """
    Main ResumeAI-Pro analysis pipeline.
    """

    pass