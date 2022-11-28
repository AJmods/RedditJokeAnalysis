import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import simpDataSets

import json

# nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

print("loading dataset")
df = simpDataSets.jokes_post()
analysis = []

print("Number of statements: ", len(df))
for idx, row in df.iterrows():
    # print(row)
    # print(row['post'])
    analysis.append(sia.polarity_scores(row['post']))
    if idx % 2000 == 0:
        print("ranking statement ", idx)

print("printing analysis")
print(analysis)
print("save analysis")

with open('ModifedData/Sentiment/jokes_post_Sentiment', 'w') as f:
    json.dump(analysis, f)
