import pandas as pd
import nltk
en_stop = set(nltk.corpus.stopwords.words('english'))
from gensim import corpora
import pickle
import simpDataSets
import gensim

def format_topics_sentences(ldamodel, corpus, texts):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        if i % 2000 == 0:
            print(f"On idx {i} of {len(ldamodel[corpus])}")
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(
                    pd.Series([int(topic_num), round(prop_topic, 4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return sent_topics_df


if __name__ == '__main__':

    text_data = []
    jokes = simpDataSets.allJokeDatesets()
    for df in jokes:
        # print("used df from year ", year)
        print("going though rows")
        for idx, row in df.iterrows():
            text_data.append(row['post'])
            if idx % 2000 == 0:
                print("On dataset # ", idx)
               #  break

    dictionary = gensim.corpora.Dictionary.load('models/jokesAllTopics/dictionary.gensim')
    corpus = pickle.load(open('models/jokesAllTopics/corpus.pkl', 'rb'))
    lda = gensim.models.ldamodel.LdaModel.load('models/jokesAllTopics/model8.gensim')

    df_topic_sents_keywords = format_topics_sentences(ldamodel=lda, corpus=corpus, texts=text_data)

    # Format
    df_dominant_topic = df_topic_sents_keywords.reset_index()
    df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']

    # Show
    df_dominant_topic.head(10)

    df_dominant_topic.to_csv("ModifedData/TopicsAlldoms.csv")
