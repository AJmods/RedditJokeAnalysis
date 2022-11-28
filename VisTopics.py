import gensim
import pickle
import pyLDAvis.gensim_models
#
# from IPython.core.display import HTML
# from IPython.core.display_functions import display

dictionary = gensim.corpora.Dictionary.load('models/jokesAllTopics/dictionary.gensim')
corpus = pickle.load(open('models/jokesAllTopics/corpus.pkl', 'rb'))
lda = gensim.models.ldamodel.LdaModel.load('models/jokesAllTopics/model8.gensim')
lda_display = pyLDAvis.gensim_models.prepare(lda, corpus, dictionary, sort_topics=False)

pyLDAvis.save_html(lda_display, 'graphs/jokes_allTopics2_topics.html')
# pyLDAvis.show(lda_display)
# viz = pyLDAvis.display(lda_display)
# dis = HTML(viz)

# display(HTML('graphs/lda_result.html'))
