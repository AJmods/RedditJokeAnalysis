import pandas as pd
from os import listdir
from os.path import isfile, join
import json


def depression_2018():
    return pd.read_csv("simpfiedData/depression_2018.csv")


def depression_2019():
    return pd.read_csv("simpfiedData/depression_2019.csv")


def depression_pre():
    return pd.read_csv("simpfiedData/depression_pre.csv")


def depression_post():
    return pd.read_csv("simpfiedData/depression_post.csv")


def jokes_2018():
    return pd.read_csv("simpfiedData/jokes_2018.csv")


def jokes_2019():
    return pd.read_csv("simpfiedData/jokes_2019.csv")


def jokes_pre():
    return pd.read_csv("simpfiedData/jokes_pre.csv")


def jokes_post():
    return pd.read_csv("simpfiedData/jokes_post.csv")


def allDepressionDatasets():
    return [depression_2018(), depression_2019(), depression_pre(), depression_post()]


def allJokeDatesets():
    return [jokes_2018(), jokes_2019(), jokes_pre(), jokes_post()]


def allDatasets():
    return [depression_2018(), depression_2019(), depression_pre(), depression_post(), jokes_2018(), jokes_2019(),
            jokes_pre(),
            jokes_post()]


def jokes_2018_sentiment():
    f = open('ModifedData/Sentiment/jokes_2018_Sentiment')  # open file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()  # close file
    return data


def jokes_2019_sentiment():
    f = open('ModifedData/Sentiment/jokes_2019_Sentiment')  # open file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()  # close file
    return data


def jokes_pre_sentiment():
    f = open('ModifedData/Sentiment/jokes_pre_Sentiment')  # open file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()  # close file
    return data


def jokes_post_sentiment():
    f = open('ModifedData/Sentiment/jokes_post_Sentiment')  # open file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()  # close file
    return data


def depression_2018_sentiment():
    f = open('ModifedData/Sentiment/depression_2018_Sentiment')  # open file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()  # close file
    return data


def depression_2019_sentiment():
    f = open('ModifedData/Sentiment/depression_2019_Sentiment')  # open file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()  # close file
    return data


def depression_pre_sentiment():
    f = open('ModifedData/Sentiment/depression_pre_Sentiment')  # open file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()  # close file
    return data


def depression_post_sentiment():
    f = open('ModifedData/Sentiment/depression_post_Sentiment')  # open file
    data = json.load(f)  # returns JSON object as a dictionary
    f.close()  # close file
    return data


def all_depression_sentiment():
    return [depression_2018_sentiment(), depression_2019_sentiment(), depression_pre_sentiment(), depression_post_sentiment()]


def all_jokes_sentiment():
    return [jokes_2018_sentiment(), jokes_2019_sentiment(), jokes_pre_sentiment(), jokes_post_sentiment()]

def jokeTopics():
    return pd.read_csv("ModifedData/doms.csv")
def jokes_2018_embeddings():
    fileDir = "embedings/jokes_2018"
    csvFiles = [fileDir + '/' + f for f in listdir(fileDir) if isfile(join(fileDir, f))]
    # df = pd.read_csv(csvFiles[0])
    # df = df.drop(df.iloc[:, 4096:len(df.columns)], axis=1)
    dfs = []
    for i in range(len(csvFiles)):  # range(len(csvFiles)):
        df1 = pd.read_csv(csvFiles[i])
        df1 = df1.drop(df1.iloc[:, 4096:len(df1.columns)], axis=1)
        dfs.append(df1)
        print("got df ", i)

    df = pd.concat(dfs, ignore_index=True)
    return df
