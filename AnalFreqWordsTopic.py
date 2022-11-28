# Import the wordcloud library
import random

import matplotlib.pyplot as plt
import nltk
import pandas as pd
from spacy.lang.en import English
from nltk.corpus import wordnet as wn
from nltk import WordNetLemmatizer
import simpDataSets
import numpy as np

en_stop = set(nltk.corpus.stopwords.words('english'))
parser = English()


def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    # tokens = [get_lemma(token) for token in tokens]
    return tokens


topic = 14
if __name__ == '__main__':
    # Join the different processed titles together.
    df = pd.read_csv(f"ModifedData/Topics/topic{topic}.csv")
    long_string = ''
    text_data = []
    for idx, row in df.iterrows():
        tokens = prepare_text_for_lda(row['Text'])
        if random.random() > 0:
            # print(tokens)
            text_data.append(tokens)
        if idx % 2000 == 0:
            print("On dataset # ", idx)

    flat_list = [item for sublist in text_data for item in sublist]
    allWordDist = nltk.FreqDist(w.lower() for w in flat_list)
    # print(allWordDist.most_common(10))
    data = allWordDist.most_common(10)
    names, values = zip(*data)  # @comment by Matthias
    # values = np.array(values)
    # values = values * (1 / len(data))
    # names = [x[0] for x in data]  # These two lines are equivalent to the the zip-command.
    # values = [x[1] for x in data] # These two lines are equivalent to the the zip-command.

    ind = np.arange(len(data))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, values, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Number of Occurrences')
    ax.set_xticks(ind + width / 2.)
    ax.set_xticklabels(names, rotation=30)


    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                    '%d' % int(height),
                    ha='center', va='bottom')


    autolabel(rects1)
    plt.title(f"Most Frequent Words for topic {topic}")
    plt.show()
