import simpDataSets
import gensim

df = simpDataSets.jokeTopics()

lda = gensim.models.ldamodel.LdaModel.load('models/jokesAll/model8.gensim')
topics = lda.print_topics(num_topics=40, num_words=10)
#print(len(topics))
for i in range(0, len(topics)):
    print(topics[i])
    # print(topics[topics['Dominant_Topic'] == 18])
    # newTopics = df[df['Dominant_Topic'] == i]
    # newTopics = newTopics.sort_values(by='Topic_Perc_Contrib')
    #
    # keywords = newTopics.iloc[0]['Keywords'].split(',')
    # topic = topics[i]
    # print(i, topic)
    # newTopics = newTopics.drop(columns=["Document_No", "Dominant_Topic"])
    # newTopics.to_csv(f"graphs/topics/topic{i}.csv")
