import pandas as pd
from collections import Counter
import re

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
    return regex.sub('', row.lower())

def prepareBagOfWords(data):
    bagOfWords = []
    bagOfWords = data['review'].apply(lambda column: Counter(column.split()))
    return bagOfWords

data = pd.read_csv('C:/Study/NLP/Practice_python/IMDB_Dataset.csv', delimiter=',')
data['output'] = data.apply(lambda row: makeOutputInt(row), axis=1)
data['review'] = data['review'].apply(preprocessInput)
print(prepareBagOfWords(data))