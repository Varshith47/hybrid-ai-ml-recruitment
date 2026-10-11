"""ML scoring for the hybrid recruitment recommender.

Uses a trained supervised model when models/job_match_model.joblib exists.
Falls back to TF-IDF cosine similarity if no trained model is available.
"""
from pathlib import Path
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import re

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "job_match_model.joblib"


def make_pair_text(job_description: str, resume_text: str) -> str:
    """Represent the pair and explicitly expose overlap/missing job terms."""
    job = job_description or ""
    resume = resume_text or ""
    tokenize = lambda text: {t for t in re.findall(r"[a-zA-Z][a-zA-Z0-9+#.]*", text.lower()) if len(t) > 1 and t not in ENGLISH_STOP_WORDS}
    job_terms = tokenize(job)
    resume_terms = tokenize(resume)
    matched = sorted(job_terms & resume_terms)
    missing = sorted(job_terms - resume_terms)
    ratio = len(matched) / max(1, len(job_terms))
    overlap_band = "high" if ratio >= 0.60 else "medium" if ratio >= 0.30 else "low"
    count_band = "many" if len(matched) >= 5 else "some" if len(matched) >= 2 else "few"
    return (
        f"JOB REQUIREMENTS: {job}\nCANDIDATE PROFILE: {resume}\n"
        f"MATCHED JOB TERMS: {' '.join(matched)}\n"
        f"JOB TERMS NOT FOUND IN PROFILE: {' '.join(missing)}\n"
        f"OVERLAP LEVEL {overlap_band} MATCHED TERM COUNT {count_band}"
    )


def score_candidates_ml(job_description: str, resumes_dict: dict) -> tuple[dict, str]:
    """Return {filename: 0..100 score}, and the method used."""
    filenames = list(resumes_dict.keys())
    if not filenames:
        return {}, "no_candidates"

    pair_texts = [make_pair_text(job_description, resumes_dict[name]) for name in filenames]
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
        probabilities = model.predict_proba(pair_texts)
        classes = list(model.classes_)
        positive_index = classes.index(1) if 1 in classes else len(classes) - 1
        classifier_scores = probabilities[:, positive_index] * 100
        # Add an explicit job-term overlap signal so the demo model's output is
        # less opaque. Replace this blend after calibration on real labeled data.
        stop_words = set(TfidfVectorizer(stop_words="english").get_stop_words() or [])
        def terms(text):
            import re
            return {t for t in re.findall(r"[a-zA-Z][a-zA-Z0-9+#.]*", (text or "").lower()) if len(t) > 1 and t not in stop_words}
        scores = []
        for name, classifier_score in zip(filenames, classifier_scores):
            job_terms = terms(job_description)
            resume_terms = terms(resumes_dict[name])
            overlap_score = 100 * len(job_terms & resume_terms) / max(1, len(job_terms))
            scores.append(0.65 * float(classifier_score) + 0.35 * overlap_score)
        return {name: round(float(score), 1) for name, score in zip(filenames, scores)}, "trained_logistic_regression_plus_overlap"

    # Baseline only: this does not constitute a trained predictive model.
    documents = [job_description or ""] + [resumes_dict[name] or "" for name in filenames]
    vectors = TfidfVectorizer(stop_words="english", ngram_range=(1, 2)).fit_transform(documents)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).ravel() * 100
    return {name: round(float(score), 1) for name, score in zip(filenames, similarities)}, "tfidf_cosine_baseline"
