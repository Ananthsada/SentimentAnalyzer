import pandas as pd
from collections import Counter
import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS


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

def removeStopWords(row, stopWords):
    return ''.join(i for i in row if i not in stopWords)

data = pd.read_csv('C:/Study/NLP/Practice_python/IMDB_Dataset_Stripped.csv', delimiter=',')
data['output'] = data.apply(lambda row: makeOutputInt(row), axis=1)
data['review'] = data['review'].astype(str)
data['review'] = data['review'].apply(preprocessInput)
print(data['review'][1])

nlp = spacy.load('en_core_web_sm')
stopwords = list(STOP_WORDS)

data['review'] = data['review'].apply(lambda row: removeStopWords(row, stopwords))
print(data['review'][1])
