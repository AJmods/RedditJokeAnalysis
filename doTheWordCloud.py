# Import the wordcloud library
import random

import nltk
from spacy.lang.en import English
from nltk.corpus import wordnet as wn
from nltk import WordNetLemmatizer
from wordcloud import WordCloud
import simpDataSets

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

    # # Join the different processed titles together.
    dfs = [simpDataSets.jokes_2018()]
    # for i in range(len(dfs[0])):
    #     msk = np.random.rand(len(allJokes[i])) < .01
    #
    #     allJokes[i] = allJokes[i][msk]
    #     df = pd.DataFrame(deprSentiment[i])
    #     deprSentiment[i] = df[msk]

    long_string = ''
    text_data = []
    for df in dfs:
        for idx, row in df.iterrows():
            tokens = prepare_text_for_lda(row['post'])
            if random.random() > 0:
                # print(tokens)
                text_data.append(tokens)
            if idx % 2000 == 0:
                print("On dataset # ", idx)

    flat_list = [item for sublist in text_data for item in sublist]
    numWords = len(flat_list)
    allWordDist = nltk.FreqDist(w.lower() for w in flat_list)
    print(allWordDist.most_common(10))
    #print(','.join(flat_list))
    long_string = ','.join(flat_list)
    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
    # Generate a word cloud
    print("createinf word cloud")
    wordcloud.generate(long_string)
    # Visualize the word cloud
    wordcloud.to_image()
    wordcloud.to_file("graphs/wordcloud/all_jokes_post_No_Lemma.png")
