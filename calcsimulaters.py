import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import simpDataSets as sd

jokes = sd.jokes_2018()
def calculate_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def PlotEmbeddings(des, pos, posPhrases, neg, negPhrases):
    # des = list(des)
    des = list(des)
    print("len des: ", len(des[0]))
    for i in range(len(des)):
        desNums = [x for x in des[i]]
        plt.scatter(desNums, np.zeros_like(desNums), label="DES")
    pos = list(pos)
    for i in range(len(pos)):
        print("len pos: ", len(pos[i]))
        print("simukatilty: ", calculate_similarity(des[0], pos[i]))
        posNums = [y for y in pos[i]]
        plt.scatter(posNums, np.zeros_like(posNums) + (i + 1), label=posPhrases[i])
    neg = list(neg)
    for i in range(len(neg)):
        negNums = [y for y in neg[i]]
        plt.scatter(negNums, np.zeros_like(negNums) - (i + 1), label=negPhrases[i])

    # plt.scatter(posNums, np.zeros_like(posNums) + 1)
    plt.legend()
    plt.show()


def getSimulitaries(i, lst):
    itemToCompareTo = lst[i]
    similarities = []
    for i in range(len(lst)):
        similarity = calculate_similarity(itemToCompareTo, lst[i])
        similarities.append(similarity)
        if similarity > .6:
            print("Joke has high simularity of ", similarity)
            print(jokes.iloc[i]['post'])
    return similarities


def plotSimilarities(sim, title='', xLabel='', yLabel=''):
    x = np.arange(len(sim))
    plt.scatter(x, sim, )

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    #df = sd.jokes_2018_embeddings()
    #df.to_csv("embedings/jokes_2018.csv")
    print("reading embeddings")
    df = pd.read_csv('embedings/jokes_2018.csv')

    #print(jokes)
    embeddings = []
    print("putting embeddings into list")
    for i in range(len(df)):
        embeddings.append(df.iloc[i].values.flatten().tolist()[1:])

    print("calculating similaires")
    jokeIdx = 5675
    sims = getSimulitaries(jokeIdx, embeddings)

    # print(calculate_similarity(embeddings[3000], embeddings[670]))
    # print(embeddings[3000])
    # print(embeddings[670])

    plotSimilarities(sims, title=str(jokes.iloc[jokeIdx]['post']), xLabel="simularity", yLabel="Joke index")
