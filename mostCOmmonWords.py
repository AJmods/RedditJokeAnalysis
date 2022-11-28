import nltk
import simpDataSets

long_string = ''
for dataSet in simpDataSets.allJokeDatesets():
    print("starting new dataset")
    for idx, row in dataSet.iterrows():
        long_string += row['post']
        if idx % 3000 == 0:
            print("on idx ", idx)

allWords = nltk.tokenize.word_tokenize(long_string)
allWordDist = nltk.FreqDist(w.lower() for w in allWords)

stopwords = nltk.corpus.stopwords.words('english')
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)

mostCommon = allWordDist.most_common(100)

import csv

# open file for writing, "w" is writing
w = csv.writer(open("MostCommonWords.csv", "w"))

# loop over dictionary keys and values
for key, val in mostCommon.items():
# write every key and value to file
    w.writerow([key, val])

print(mostCommon)
