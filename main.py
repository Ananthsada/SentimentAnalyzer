import pandas as pd
from collections import Counter
import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer


# Funtion to return 1 or 0 as output
# Input: Entire row
# Output: Integer
def makeOutputInt(row):
    if row['sentiment'] == 'positive':
        return 1
    else:
        return 0

# Function to do the preprocessing on input text
# Input: Input string
# Output: Preprocessed string
def preprocessInput(row, tokenizer):
    regex = re.compile('[^a-zA-Z ]')
    output = regex.sub('', row.lower())

    tokens = tokenizer(output)

    filtered_tokens = " ".join(token.text for token in tokens if not token.is_stop)
    return filtered_tokens


data = pd.read_csv('C:/Study/NLP/Practice_python/IMDB_Dataset_Stripped.csv', delimiter=',')
data['output'] = data.apply(lambda row: makeOutputInt(row), axis=1)
data['review'] = data['review'].astype(str)
print(len(data))

nlp = spacy.load('en_core_web_sm')
tokenizer = nlp.tokenizer

data['review'] = data['review'].apply(lambda row: preprocessInput(row, tokenizer))

vectorizer = TfidfVectorizer()
vectorizedOut =vectorizer.fit_transform(data['review'])
print(vectorizedOut.todense())

