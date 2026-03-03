from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_vectors(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform([resume_text, jd_text])
    return matrix

def compute_similarity(matrix):
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(score * 100, 2)