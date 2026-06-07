#Current Version (TF-IDF)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(
        resume_text,
        job_description
):

    vectorizer = TfidfVectorizer()#this will convert the text into a matrix of TF-IDF features and tells us how important a word is to a document in a collection of documents. It does this by calculating the term frequency (TF) and inverse document frequency (IDF) for each word in the text, and then multiplying these two values together to get the TF-IDF score for each word. The resulting matrix will have rows corresponding to the documents (in this case, the resume and job description) and columns corresponding to the unique words in the combined text. The values in the matrix will represent the TF-IDF scores for each word in each document.

    matrix = vectorizer.fit_transform(
        [resume_text, job_description]
    )

    score = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    return round(score * 100, 2)