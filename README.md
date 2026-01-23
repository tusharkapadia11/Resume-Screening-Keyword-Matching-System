
---

# ATS Resume Screening & Analytics

## Overview

An AI-powered **Applicant Tracking System (ATS)** that automates resume screening using **NLP and Machine Learning**. It evaluates resumes against job descriptions and generates match scores, skill insights, and candidate rankings.

---

## Problem Statement

Manual resume screening is time-consuming, inconsistent, and difficult to scale.

---

## Solution

Automated ATS that analyzes resumes and shortlists candidates based on relevance to job descriptions.

---

## Key Features

* Resume parsing
* Job–resume matching
* Resume match score (%)
* Skill extraction
* Candidate ranking

---

## Tech Stack

* **Language:** Python
* **ML/NLP:** Scikit-learn, TF-IDF
* **Data:** Pandas, NumPy
* **Web:** Flask / Streamlit

---

## Workflow

Resume & Job Description → Text Preprocessing → TF-IDF → Similarity Calculation → Analytics Output

---

## Results

* Resume match percentage
* Skill match insights
* Ranked candidate list

---

## Project Structure

```text
ATS_Resume_Screening_Analytics-main/
├── app.py
├── templates/
├── static/
├── resumes/
├── requirements.txt
└── README.md
```

---

## Steps to Run the Project

```bash
# 1. Clone the repository
git clone <repository-url>

# 2. Navigate to the project folder
cd ATS_Resume_Screening_Analytics-main

# 3. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python app.py
```

Open the app in your browser (usually `http://127.0.0.1:5000`).

---

## Tags

`ATS` `NLP` `MachineLearning` `ResumeScreening` `AIRecruitment`

---
