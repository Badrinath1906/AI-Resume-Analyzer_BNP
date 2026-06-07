#Purpose: Clean text
#Remove stopwords
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z\s]',
        '',
        text
    )

    return text


def remove_stopwords(text):

    stop_words = set(
        stopwords.words('english')
    )

    words = word_tokenize(text)

    filtered = [
        word
        for word in words
        if word not in stop_words
    ]

    return " ".join(filtered)