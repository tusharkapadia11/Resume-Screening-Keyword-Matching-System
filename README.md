# 📄 ATS Resume Screening & Analytics

## AI-powered Resume Screening Using NLP to Rank Candidates Against Job Descriptions

An Applicant Tracking System (ATS) that automatically evaluates resumes against job descriptions using Natural Language Processing (NLP), helping recruiters identify the most relevant candidates quickly and consistently.

---

# Business Context

Recruiters often receive hundreds of resumes for a single position, making manual screening slow and inconsistent. This project was developed to automate the initial screening process by comparing candidate resumes with job descriptions and generating objective relevance scores. The system assists recruiters in identifying qualified candidates while reducing manual effort.

---

# Dataset

The application processes two user-provided inputs rather than relying on a fixed dataset.

| Source          | Description                                      |
| --------------- | ------------------------------------------------ |
| Resume          | PDF or text resume uploaded by the user          |
| Job Description | Job requirements entered or uploaded by the user |

### Data Characteristics

* Grain: One candidate resume
* Input Type: Unstructured text
* Output: Resume match score, extracted skills, candidate ranking
* Domain: Recruitment / Human Resources

---

# Methodology

The application follows a Natural Language Processing pipeline to measure resume relevance.

1. Resume parsing and text extraction
2. Text preprocessing

   * Lowercasing
   * Stop-word removal
   * Tokenization
3. TF-IDF Vectorization
4. Cosine Similarity calculation
5. Resume match score generation
6. Candidate ranking based on similarity

### Why TF-IDF?

TF-IDF was selected because it is lightweight, interpretable, and performs well for document similarity tasks. Compared to deep learning approaches, it requires significantly less computational power while providing reliable matching for keyword-driven recruitment scenarios.

---

# Key Features

* Resume parsing
* Job description matching
* Resume similarity score
* Skill extraction
* Candidate ranking
* Interactive Streamlit interface

---

# Sample Output

The system generates:

* Resume Match Score (%)
* Matching Skills
* Missing Skills
* Candidate Ranking
* Resume Relevance Summary

---

# Recommendations

This application can help recruitment teams:

* Reduce manual resume screening time.
* Improve consistency during initial candidate shortlisting.
* Quickly identify resumes matching required technical skills.
* Prioritize high-scoring candidates for further evaluation.

---

# Limitations & Assumptions

* Matching quality depends on the quality of the job description.
* TF-IDF focuses on textual similarity and may not capture semantic meaning.
* The system does not evaluate candidate experience, interview performance, or cultural fit.
* Skill extraction is based on textual content present in the uploaded resume.

---

# Project Structure

```text
ATS_Resume_Screening_Analytics-main/
│
├── app.py
├── templates/
├── static/
├── resumes/
├── requirements.txt
└── README.md
```

---

# Installation

```bash
git clone <repository-url>

cd ATS_Resume_Screening_Analytics-main

python -m venv venv

# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---

# Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* TF-IDF
* Cosine Similarity
* NLP

---

# License

This project is intended for educational and portfolio purposes.
