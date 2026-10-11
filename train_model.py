"""Train a supervised resume/job-match classifier.

CSV schema: job_description,resume_text,label
label must be 1 (suitable) or 0 (not suitable).
"""
from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from ml_engine import make_pair_text, MODEL_PATH

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "training_data.csv"


def main():
    if not DATA_PATH.exists():
        raise SystemExit("training_data.csv not found. Create it with job_description,resume_text,label columns.")
    df = pd.read_csv(DATA_PATH).dropna(subset=["job_description", "resume_text", "label"])
    required = {"job_description", "resume_text", "label"}
    if not required.issubset(df.columns):
        raise SystemExit("CSV must contain: job_description,resume_text,label")
    df["label"] = df["label"].astype(int)
    if set(df["label"].unique()) != {0, 1}:
        raise SystemExit("Training data must contain both labels 0 and 1.")
    if len(df) < 12 or df["label"].value_counts().min() < 3:
        raise SystemExit("Use at least 12 labeled examples and at least 3 examples for each label; more is much better.")

    X = [make_pair_text(j, r) for j, r in zip(df["job_description"], df["resume_text"])]
    y = df["label"].to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=30000, sublinear_tf=True)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42)),
    ])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Held-out test metrics (small datasets have high uncertainty):")
    print(f"Accuracy : {accuracy_score(y_test, pred):.3f}")
    print(f"Precision: {precision_score(y_test, pred, zero_division=0):.3f}")
    print(f"Recall   : {recall_score(y_test, pred, zero_division=0):.3f}")
    print(f"F1       : {f1_score(y_test, pred, zero_division=0):.3f}")
    print(classification_report(y_test, pred, zero_division=0))
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Saved trained model to: {MODEL_PATH}")
    print("Note: metrics are only meaningful if labels are reliable and the test examples represent real cases.")

if __name__ == "__main__":
    main()
