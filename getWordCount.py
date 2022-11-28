# Import the wordcloud library
import random

import matplotlib.pyplot as plt
import nltk
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


if __name__ == '__main__':

    # Join the different processed titles together.
    dfs = simpDataSets.allJokeDatesets()
    long_string = ''
    text_data = []
    wordCounts = []
    for df in dfs:
        for idx, row in df.iterrows():
            tokens = prepare_text_for_lda(row['post'])
            wordCounts.append(len(tokens))
            if idx % 2000 == 0:
                print("on idx ", idx)

    print(wordCounts)
    print("making the worst hist in history")
    plt.scatter(np.arange(len(wordCounts)), wordCounts, s=1)
    plt.title("Word Counts for each joke")
    plt.ylabel("Word Count")
    plt.ylim(0,200)
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    plt.show()
