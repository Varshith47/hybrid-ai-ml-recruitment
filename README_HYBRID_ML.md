# Hybrid AI + ML Recruitment Recommendation Tool

## What changed
- Keeps the existing Flask app and Gemini-based analysis.
- Adds a supervised Scikit-learn pipeline: TF-IDF (unigrams + bigrams) + Logistic Regression.
- Uses the model to estimate a candidate/job suitability score.
- Blends the ML score with the Gemini score (50% ML + 50% Gemini) for the final ranking.
- If the trained model file is missing, the app falls back to TF-IDF cosine similarity and labels that mode as a baseline, not a trained classifier.

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
# Edit .env and set your own GeminiApi key
python train_model.py
python main.py
```
Open the local URL printed by Flask.

## Training data
`training_data.csv` contains **synthetic demonstration pairs** generated for the prototype. The reported test metrics measure performance on held-out synthetic examples only; they are not evidence of real-world hiring accuracy. For a credible model, replace it with reviewed, permissioned, representative labeled job/resume pairs. Keep the same columns:
- `job_description`: job requirements text
- `resume_text`: candidate profile text
- `label`: `1` suitable, `0` unsuitable, based on a documented labeling policy

Use substantially more examples, avoid duplicate/leaked candidates across train/test, evaluate on a representative held-out set, and check fairness. Do not use protected attributes or proxies as ranking criteria. A match score must support human review, not automatically reject applicants.

## How scoring works
- Trained classifier: predicts probability for label `1`.
- Fallback: TF-IDF cosine similarity between the job description and resume.
- Hybrid score: `0.5 * ML score + 0.5 * Gemini score`.
The two score types are not inherently calibrated to the same meaning, so the 50/50 blend is a prototype default. Validate/calibrate weights against reviewed examples before real use.

## Security note
The ZIP created for sharing intentionally excludes your original `.env`, SQLite user database, and uploaded resumes. Add your own `.env` locally; never share API keys or candidate personal data.
