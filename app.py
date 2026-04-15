from flask import Flask, render_template, request
import os
import pandas as pd
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import docx2txt
import PyPDF2

# Download NLTK resources (only first time)
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load dataset
df = pd.read_csv('data/AI_Resume_Screening.csv')

# -------------------------------
# 🔹 Extract text from resume
# -------------------------------
def extract_text(file_path):
    text = ""

    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()

    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)

    return text


# -------------------------------
# 🔹 Preprocess text
# -------------------------------
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    filtered = [word for word in tokens if word not in stop_words]

    return filtered


# -------------------------------
# 🔹 Get skills for role
# -------------------------------
def get_role_skills(role):
    role_df = df[df['Job Role'].str.lower() == role.lower()]
    if role_df.empty:
        return []

    skills = ",".join(role_df['Skills'].astype(str))
    skills_list = [skill.strip().lower() for skill in skills.split(",")]
    return list(set(skills_list))


# -------------------------------
# 🔹 Analyze Resume
# -------------------------------
def analyze_resume(resume_text, role):
    tokens = preprocess_text(resume_text)
    role_skills = get_role_skills(role)

    matched = []
    missing = []

    for skill in role_skills:
        if skill in tokens:
            matched.append(skill)
        else:
            missing.append(skill)

    score = 0
    if len(role_skills) > 0:
        score = (len(matched) / len(role_skills)) * 100

    return score, matched, missing


# -------------------------------
# 🔹 Suggestions
# -------------------------------
def generate_suggestions(missing_skills):
    suggestions = []
    for skill in missing_skills[:5]:
        suggestions.append(f"Add {skill} to your resume")

    if not suggestions:
        suggestions.append("Great! Your resume matches well.")

    return suggestions


# -------------------------------
# 🔹 Routes
# -------------------------------

@app.route('/')
def home():
    roles = df['Job Role'].unique()
    return render_template('index.html', roles=roles)


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    role = request.form['role']

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        text = extract_text(filepath)

        score, matched, missing = analyze_resume(text, role)
        suggestions = generate_suggestions(missing)

        return render_template('result.html',
                               score=round(score, 2),
                               matched=matched,
                               missing=missing,
                               suggestions=suggestions)

    return "Error: No file uploaded"


# -------------------------------
# 🔹 Run App
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)