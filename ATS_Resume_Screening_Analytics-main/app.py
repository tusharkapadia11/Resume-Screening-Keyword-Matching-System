from flask import Flask, render_template, request
import os
import docx2txt
import PyPDF2

app = Flask(__name__)

# Config
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

# ATS Keywords
ATS_KEYWORDS = [
    "python", "django", "flask", "sql",
    "data", "machine learning", "api"
]

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Extract text from resume
def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text

    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)

    return ""

# Calculate ATS score
def calculate_ats_score(text):
    text = text.lower()
    matched = sum(1 for kw in ATS_KEYWORDS if kw in text)
    score = (matched / len(ATS_KEYWORDS)) * 100
    return round(score, 2)

# Main route
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    score = None

    if request.method == "POST":
        file = request.files.get("file")

        if not file or file.filename == "":
            message = "No file selected"
        else:
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            text = extract_text(path)
            if text.strip() == "":
                message = "Could not read the file"
            else:
                score = calculate_ats_score(text)
                message = "Resume uploaded successfully"

    return render_template("index.html", message=message, score=score)

if __name__ == "__main__":
    app.run(debug=True)
