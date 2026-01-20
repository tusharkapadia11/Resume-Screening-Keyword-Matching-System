'''
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
import os
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__)
app.config["SECRET_KEY"] = "mulasaag"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return f"File {file.filename} uploaded successfully!"
    return render_template('index.html')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {"pdf", "docx"}

KEYWORDS = {
    "python": 10,
    "django": 8,
    "sql": 6,
    "api": 5,
    "data": 4
}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadForm(FlaskForm):
    file = FileField("Upload Resume", validators=[InputRequired()])
    submit = SubmitField("Check ATS Score")

def extract_text(path):
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        return " ".join([p.extract_text() or "" for p in reader.pages])
    elif path.endswith(".docx"):
        doc = Document(path)
        return " ".join([p.text for p in doc.paragraphs])
    return ""

def calculate_score(text):
    score = 0
    text = text.lower()
    for k, v in KEYWORDS.items():
        if k in text:
            score += v
    return score

@app.route("/", methods=["GET", "POST"])
def index():
    form = UploadForm()
    score = None

    if form.validate_on_submit():
        file = form.file.data
        if allowed_file(file.filename):
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            text = extract_text(path)
            score = calculate_score(text)

    return render_template("index.html", form=form, score=score)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
    '''

from flask import Flask, render_template, request
import os
import docx2txt  # for .docx
import PyPDF2    # for .pdf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Simple ATS keywords
ATS_KEYWORDS = ["Python", "Django", "Flask", "JavaScript", "React", "SQL", "Data", "Machine Learning"]

# Helper function to extract text from uploaded file
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        text = ""
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
        return text
    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
        return text
    else:
        return ""

# Simple ATS score based on keywords
def calculate_ats_score(text):
    text_lower = text.lower()
    matched = 0
    for kw in ATS_KEYWORDS:
        if kw.lower() in text_lower:
            matched += 1
    score = (matched / len(ATS_KEYWORDS)) * 100
    return round(score, 2)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    message = ""
    score = None
    if request.method == 'POST':
        if 'file' not in request.files:
            message = "No file part"
        else:
            file = request.files['file']
            if file.filename == '':
                message = "No selected file"
            else:
                filename = file.filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                text = extract_text(file_path)
                if text.strip() == "":
                    message = "Cannot read text from this file."
                else:
                    score = calculate_ats_score(text)
                    message = f"File {filename} uploaded successfully!"
    return render_template('index.html', message=message, score=score)

if __name__ == '__main__':
    # Make sure uploads folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
