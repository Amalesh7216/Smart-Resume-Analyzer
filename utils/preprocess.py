import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()


# -------------------------------
# 🔹 Clean Text
# -------------------------------
def clean_text(text):
    """
    Remove special characters, numbers, and extra spaces
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# -------------------------------
# 🔹 Tokenization
# -------------------------------
def tokenize_text(text):
    """
    Convert text into tokens (words)
    """
    return word_tokenize(text)


# -------------------------------
# 🔹 Remove Stopwords
# -------------------------------
def remove_stopwords(tokens):
    """
    Remove common English stopwords
    """
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens


# -------------------------------
# 🔹 Lemmatization
# -------------------------------
def lemmatize_tokens(tokens):
    """
    Convert words to base form (e.g., running → run)
    """
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized


# -------------------------------
# 🔹 Full Preprocessing Pipeline
# -------------------------------
def preprocess_text(text):
    """
    Complete preprocessing:
    Cleaning → Tokenization → Stopword Removal → Lemmatization
    """
    text = clean_text(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    return tokens


# -------------------------------
# 🔹 Convert Tokens to String
# -------------------------------
def tokens_to_text(tokens):
    """
    Convert tokens back to text
    """
    return " ".join(tokens)