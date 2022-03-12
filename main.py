import pandas as pd
from collections import Counter
import re

stopwords = ['the', 'a', 'an', 'and', 'or', 'is', 'was', 'be', 'have', 'had', 'been', 'are', 'were', 'could', 'would',
             'of', 'to', 'in', 'at', 'this', 'that', 'by', 'for','there', 'here', 'as', 'it', 'as', 'with', 'but', 'i',
             'he', 'she', 'her', 'him', 'them', 'we', 'us', 'on', 'nan', 'you', 'br', 'his', 'its']

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
    return ' '.join(i for i in output.split() if i not in stopwords)
    #return output

def prepareBagOfWords(bagOfWords, data):
    #bagOfWords = data['review'].apply(lambda column: Counter(column.split()))
    bagOfWords.extend(data.split())

#def prepareDataset(bagOfWords, row):


data = pd.read_csv('C:/Study/NLP/Practice_python/IMDB_Dataset_Stripped.csv', delimiter=',')
data['output'] = data.apply(lambda row: makeOutputInt(row), axis=1)
data['review'] = data['review'].astype(str)
data['review'] = data['review'].apply(preprocessInput)
bagOfWords=[]
data['review'].apply(lambda row: prepareBagOfWords(bagOfWords, row))
#counter = Counter(bagOfWords)
index = 0

new_data = pd.DataFrame()

for each in bagOfWords:
    bagList = []
    bagList.append(sum(1 for i in data.iloc[index]['review'].split() if i == each))
    index = index + 1
    #print(bagList)
    new_data[each] = bagList


