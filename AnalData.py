# import dataFiles
import pandas as pd
import statistics

pd.set_option('display.max_columns', None)
jokes_2018 = pd.read_csv("data/depression_2018_features_tfidf_256.csv")
jokes_2019 = pd.read_csv("data/depression_2019_features_tfidf_256.csv")
jokes_pre = pd.read_csv("data/depression_pre_features_tfidf_256.csv")
jokes_post = pd.read_csv("data/depression_post_features_tfidf_256 (1).csv")

jokes = [jokes_2018, jokes_2019, jokes_pre, jokes_post]
# avgWords = []
# avgChars = []
# avgLongWords = []
# avgSyllables = []
# avgMonoSyllableWords = []
# avgPolySyyableWords = []
# avg_isolation = []
# avgSuicidalityTotal = []
# for jokeData in jokes:
#     avgWords.append(jokeData["n_words"].mean())
#     avgChars.append(jokeData["n_chars"].mean())
#     avgLongWords.append(jokeData["n_long_words"].mean())
#     avgMonoSyllableWords.append(jokeData["n_monosyllable_words"].mean())
#     avgPolySyyableWords.append(jokeData["n_polysyllable_words"].mean())

averages = []
for jokeData in jokes:
    averageDict = {}
    for (columnName, columnData) in jokeData.items():
        # print('name', columnName, 'data', columnData[0])
        # print("tpye: ", type(columnData))
        try:
            averageDict[columnName] = statistics.mean(columnData)
        except:
            pass
            # print(columnName, " Not nums")
    averages.append(averageDict)

print(averages)
print(jokes_2018.head())
