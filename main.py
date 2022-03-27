import pandas as pd
from collections import Counter
import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokenizer import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer


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
def preprocessInput(row):
    regex = re.compile('[^a-zA-Z ]')
    output = regex.sub('', row.lower())
    return output


data = pd.read_csv('C:/Study/NLP/Practice_python/IMDB_Dataset_Stripped.csv', delimiter=',')
data['output'] = data.apply(lambda row: makeOutputInt(row), axis=1)
data['review'] = data['review'].astype(str)
data['review'] = data['review'].apply(preprocessInput)

nlp = spacy.load('en_core_web_sm')
stopwords = list(STOP_WORDS)

joinedList = ""
for each in data['review']:
    joinedList = joinedList + each

tokenizer = nlp.tokenizer
tokens = tokenizer(joinedList)

filtered_tokens = [token for token in tokens if not token.is_stop]

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(filtered_tokens)