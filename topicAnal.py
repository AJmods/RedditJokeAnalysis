import spacy

# spacy.load('en_core_web_sm')
from spacy.lang.en import English

parser = English()

from nltk.stem.wordnet import WordNetLemmatizer
import nltk

nltk.download('wordnet')
from nltk.corpus import wordnet as wn

nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))

nltk.download('omw-1.4')

from gensim import corpora
import pickle

import random
import simpDataSets
import gensim
import pyLDAvis.gensim_models


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
    tokens = [get_lemma(token) for token in tokens]
    return tokens


years = ["2018", '2019', 'pre', 'post']
if __name__ == '__main__':

    # year = years[0]
    text_data = []
    for year in years:
        df = None
        if year == '2018':
            df = simpDataSets.jokes_2018()
        elif year == '2019':
            df = simpDataSets.jokes_2019()
        elif year == 'pre':
            df = simpDataSets.jokes_pre()
        elif year == 'post':
            df = simpDataSets.jokes_post()

        print("used df from year ", year)
        print("going though rows")
        for idx, row in df.iterrows():
            tokens = prepare_text_for_lda(row['post'])
            if random.random() > 0:
                # print(tokens)
                text_data.append(tokens)
            if idx % 2000 == 0:
                print("On dataset # ", idx, "for year ", year)

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    year = 'AllTopics'
    pickle.dump(corpus, open(f'models/jokes{year}/corpus.pkl', 'wb'))
    dictionary.save(f'models/jokes{year}/dictionary.gensim')

    NUM_TOPICS = 400
    print("Making model")
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
    ldamodel.save(f'models/jokes{year}/model8.gensim')
    topics = ldamodel.print_topics(num_words=4)

    lda = gensim.models.ldamodel.LdaModel.load(f'models/jokes{year}/model8.gensim')
    lda_display = pyLDAvis.gensim_models.prepare(lda, corpus, dictionary, sort_topics=False)
    pyLDAvis.save_html(lda_display, f'graphs/jokes_{year}_topics.html')
    for topic in topics:
        print(topic)
