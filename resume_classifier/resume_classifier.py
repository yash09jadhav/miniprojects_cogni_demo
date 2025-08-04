import os
import fitz  
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def load_resumes(folder_path):
    resumes = {}
    for file in os.listdir(folder_path):
        with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
            resumes[file] = f.read()
    return resumes

with open('job_description.txt', 'r', encoding='utf-8') as f:
    job_desc = f.read()

def rank_resumes(resumes, job_desc):
    docs = [job_desc] + list(resumes.values())
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(docs)
    scores = cosine_similarity(tfidf_matrix[:1], tfidf_matrix[1:]).flatten()

    ranked = sorted(zip(resumes.keys(), scores), key=lambda x: x[1], reverse=True)
    return ranked

# ---------- pipeline ----------
resume_texts = load_resumes("resumes")
ranked_resumes = rank_resumes(resume_texts, job_desc)

df = pd.DataFrame(ranked_resumes)
print(df)

'''
df.to_csv("ranked_resumes.csv", index=False)
'''