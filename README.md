# 🤖 AI-Powered Talent Job Fit Recommendation & Recruitment Optimization Tool

An AI-powered recruitment platform that analyzes job descriptions and candidate resumes to help recruiters identify, evaluate, and rank suitable candidates more efficiently.

**Live Demo:** [Open the Application](https://hybrid-ai-ml-recruitment.onrender.com/)

**GitHub Repository:** [hybrid-ai-ml-recruitment](https://github.com/Varshith47/hybrid-ai-ml-recruitment)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [System Architecture](#-system-architecture)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Installation and Setup](#-installation-and-setup)
- [Environment Configuration](#-environment-configuration)
- [Run the Application](#-run-the-application)
- [Deploy on Render](#-deploy-on-render)
- [Machine Learning Approach](#-machine-learning-approach)
- [Future Enhancements](#-future-enhancements)
- [Security and Limitations](#-security-and-limitations)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

## 📖 Overview

The AI-Powered Talent Job Fit Recommendation & Recruitment Optimization Tool is a web application designed to streamline the initial stages of recruitment.

Recruiters can provide a job description and upload candidate resumes. The application extracts resume content, analyzes candidate profiles, evaluates job relevance, and produces a ranked list of candidates with matching scores and explanations.

The project combines Python-based web development, machine learning techniques, resume processing, and Google's Gemini generative AI API to support recruitment decisions.

## ❗ Problem Statement

Traditional recruitment often requires recruiters to manually review large numbers of resumes. This process can be time-consuming, repetitive, and difficult to scale.

Common challenges include:

- Reviewing large volumes of candidate applications.
- Identifying relevant technical skills and experience.
- Comparing candidates against job requirements.
- Finding missing or underrepresented qualifications.
- Providing consistent explanations for candidate rankings.

This project aims to reduce repetitive screening work by providing automated resume analysis and job-fit recommendations.

## 🎯 Objectives

- Automate the initial screening of candidate resumes.
- Extract useful information from PDF, DOCX, and TXT files.
- Compare candidate profiles with job descriptions.
- Rank candidates according to job relevance.
- Generate understandable candidate evaluation summaries.
- Identify candidate strengths and potential skill gaps.
- Help recruiters make more informed shortlisting decisions.

## ✨ Key Features

### 1. User Authentication

- User registration and login.
- Password hashing using Flask-Bcrypt.
- Authentication management using Flask-Login.
- Database integration through Flask-SQLAlchemy.

### 2. Resume Upload and Text Extraction

- Upload candidate resumes in supported document formats.
- Extract text from PDF files.
- Process DOCX documents.
- Read plain-text resumes.
- Prepare extracted resume content for analysis.

### 3. Job Description Analysis

- Accept a job description as input.
- Identify relevant qualifications, skills, and experience requirements.
- Compare candidate resume content against job-related criteria.

### 4. AI-Powered Candidate Ranking

- Evaluate the relevance of candidates to the specified job.
- Generate candidate match scores.
- Rank applicants based on the analysis.
- Present a shortlist of potentially suitable candidates.

### 5. Candidate Insights

The AI analysis is designed to provide useful recruitment insights, such as:

- Candidate strengths.
- Relevant skills and qualifications.
- Potential skill gaps.
- Job-fit explanations.
- Suggested interview questions.

The availability and completeness of individual insights depend on the implemented analysis workflow and the quality of the extracted resume text.

### 6. Machine Learning Integration

- Python-based ML processing.
- A dedicated ML engine module.
- A model training script and training dataset.
- A saved model artifact for supported prediction workflows.

### 7. Web-Based Interface

- Browser-accessible application.
- Registration and login pages.
- Resume and job-description workflow.
- Server-side processing using Flask.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Flask |
| Authentication | Flask-Login, Flask-Bcrypt |
| Database ORM | Flask-SQLAlchemy |
| Database | SQLite in the current configuration |
| Machine Learning | Scikit-learn, Pandas |
| Generative AI | Google Gemini API |
| Resume Processing | PyPDF2, PyMuPDF, docx2txt |
| Model Persistence | Joblib |
| Application Server | Gunicorn |
| Version Control | Git and GitHub |
| Deployment | Render |

## 🏗️ System Architecture

```text
Recruiter
   |
   v
Web Application
   |
   v
Flask Backend
   |
   +----------------------+
   |                      |
   v                      v
Authentication       Resume Processing
   |                      |
   v                      v
SQLAlchemy DB        Extracted Resume Text
                          |
                          v
                  ML / AI Analysis
                          |
                 +--------+--------+
                 |                 |
                 v                 v
           ML Processing      Gemini API
                 |                 |
                 +--------+--------+
                          |
                          v
                Candidate Evaluation
                          |
                          v
                Ranked Recommendations
```

The diagram represents the intended high-level workflow. Exact processing steps depend on the current implementation and configured model.

## ⚙️ How It Works

1. **Register or log in:** The recruiter accesses the application through the authentication pages.
2. **Enter the job description:** Provide the role requirements and relevant qualifications.
3. **Upload resumes:** Submit candidate resumes in supported formats.
4. **Extract text:** The backend reads text from uploaded documents.
5. **Analyze candidates:** The application evaluates the extracted information against the job description.
6. **Generate recommendations:** The analysis produces candidate rankings and available explanations.
7. **Review results:** The recruiter uses the recommendations as support for further screening and interviews.

## 📂 Project Structure

```text
hybrid-ai-ml-recruitment/
│
├── main.py
│   └── Flask application, routes, and application logic
│
├── ml_engine.py
│   └── Machine learning and candidate analysis logic
│
├── train_model.py
│   └── Model training workflow
│
├── training_data.csv
│   └── Dataset used by the training workflow
│
├── models/
│   └── Saved machine learning model artifacts
│
├── templates/
│   ├── app.html
│   ├── login.html
│   └── register.html
│
├── requirements.txt
│   └── Python dependencies
│
├── .env.example
│   └── Example environment configuration
│
├── .gitignore
│   └── Files excluded from version control
│
└── README.md
    └── Project documentation
```

## 💻 Installation and Setup

### Prerequisites

Install the following software before running the project locally:

- Python 3.10 or another Python version compatible with the project's dependencies.
- Git.
- A Google Gemini API key if using Gemini-powered analysis.
- A code editor such as Visual Studio Code.

The Python version required for deployment must be compatible with all dependencies listed in `requirements.txt`.

### Step 1: Clone the repository

Open Command Prompt or a terminal and run:

```bash
git clone https://github.com/Varshith47/hybrid-ai-ml-recruitment.git
```

Navigate to the project directory:

```bash
cd hybrid-ai-ml-recruitment
```

### Step 2: Create a virtual environment

On Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If Gunicorn is not included in the requirements file and you need it for deployment, install it with:

```bash
pip install gunicorn
```

### Step 4: Configure environment variables

Create a local `.env` file if the application uses environment-based configuration.

Use `.env.example` as a reference for the expected variable names. Never commit the actual `.env` file or your API key.

### Step 5: Start the application

For local development:

```bash
python main.py
```

If the application starts successfully, open the local address printed in the terminal. For a typical Flask development configuration, this is:

```text
http://127.0.0.1:5000/
```

The actual address and port depend on the application's configuration.

## 🔐 Environment Configuration

The application may require a Gemini API key and other environment-specific settings.

For example, if `main.py` reads the variable `GEMINI_API_KEY`, configure it in your local environment or deployment settings.

Windows Command Prompt:

```cmd
set GEMINI_API_KEY=YOUR_GEMINI_API_KEY
python main.py
```

PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
python main.py
```

Replace the placeholder with your own key. Do not publish the real key in source code, screenshots, GitHub commits, or frontend JavaScript.

If the application expects a different variable name, use the name defined in its code.

## ☁️ Deploy on Render

The application can be deployed as a Python web service on Render.

### Step 1: Connect GitHub

1. Sign in to [Render](https://render.com/).
2. Select **New → Web Service**.
3. Connect your GitHub account.
4. Select the `hybrid-ai-ml-recruitment` repository.
5. Select the `main` branch.

### Step 2: Configure the service

Use the following settings, subject to your application's configuration:

| Setting | Value |
|---|---|
| Runtime | Python |
| Branch | `main` |
| Root Directory | Blank if `main.py` is at the repository root |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn main:app` |
| Instance | Free plan for testing |

The start command assumes that `main.py` exposes a Flask application object named `app` and Gunicorn is installed.

### Step 3: Configure environment variables

In the Render service dashboard, open **Environment** and add the environment variables required by your application, including the Gemini API key if needed.

### Step 4: Deploy

1. Create the service.
2. Wait for dependency installation and deployment.
3. Review the logs for errors.
4. Open the public Render URL.
5. Test registration, login, and the main application workflow.

### Live Application

[https://hybrid-ai-ml-recruitment.onrender.com/](https://hybrid-ai-ml-recruitment.onrender.com/)

**Note:** The live application may be temporarily unavailable during deployments or troubleshooting. A successful deployment alone does not guarantee that all features work correctly.

## 🧠 Machine Learning Approach

The project includes a machine learning engine, a training script, a dataset, and saved model artifacts.

The general objective of the ML workflow is to support the evaluation of candidate profiles in relation to job requirements.

The application also integrates Gemini for contextual AI-based analysis where configured.

### Model Training

The training script is:

```bash
python train_model.py
```

Run this command from the project directory after installing the required dependencies.

The resulting model artifact, its features, and its evaluation metrics depend on the training code and dataset.

### Model Evaluation

A reliable evaluation should use representative, labeled data and an appropriate validation strategy. Useful measurements may include precision, recall, F1-score, and other metrics suited to the defined prediction task.

**Important:** Training on demonstration or synthetic data does not establish real-world recruitment accuracy. Model performance should be measured on suitable held-out data before making accuracy claims.

## 🚀 Future Enhancements

Potential improvements include:

- Persistent production database using PostgreSQL.
- Recruiter dashboard with candidate summaries.
- More advanced resume parsing and structured candidate profiles.
- Explainable candidate matching and skill-gap analysis.
- Improved model evaluation and validation.
- Candidate search, filtering, and comparison.
- Downloadable recruitment reports.
- Automated testing and continuous integration.
- Improved upload validation and file-size limits.
- Role-based authorization and audit logging.
- Integration with job portals and recruitment management systems.

## 🔒 Security and Limitations

- **Database persistence:** The current SQLite configuration may not provide reliable persistent storage on a cloud service with an ephemeral filesystem. Use a persistent database for production.
- **AI-generated results:** AI explanations and match scores can be incomplete or incorrect. Recruiters should verify important findings.
- **Recruitment fairness:** Resume ranking must not be treated as an automatic hiring decision. Evaluate for bias and avoid using protected characteristics in candidate selection.
- **API usage:** Gemini availability, quotas, pricing, and response quality depend on the configured account and service.
- **Resume privacy:** Resumes contain personal information. Obtain appropriate permission, restrict access, and establish retention and deletion procedures.
- **File validation:** Uploaded files should be validated and size-limited. Do not assume a file is safe solely because it has a PDF or DOCX extension.
- **Deployment:** Free hosting can have resource limitations, cold starts, and storage restrictions.
- **Demo status:** The application should be tested end to end before being used with real candidate information.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the changes locally.
5. Submit a pull request describing the improvement.

## 👨‍💻 Author

**Varshith Reddy Nimma**

B.Tech Computer Science and Engineering

GitHub: [@Varshith47](https://github.com/Varshith47)

## 📄 License

No license has been specified for this repository yet. Add a `LICENSE` file before declaring the project open source or granting permissions for reuse.

---

⭐ If you find this project useful, consider starring the repository.

**Built with Python, Flask, machine learning, and generative AI.**
