import pandas as pd

depression_2018 = pd.read_csv("data/depression_2018_features_tfidf_256.csv")
depression_2019 = pd.read_csv("data/depression_2019_features_tfidf_256.csv")
depression_pre = pd.read_csv("data/depression_pre_features_tfidf_256.csv")
depression_post = pd.read_csv("data/depression_post_features_tfidf_256 (1).csv")

jokes_2018 = pd.read_csv("data/jokes_2018_features_tfidf_256.csv")
jokes_2019 = pd.read_csv("data/jokes_2019_features_tfidf_256.csv")
jokes_pre = pd.read_csv("data/jokes_pre_features_tfidf_256.csv")
jokes_post = pd.read_csv("data/jokes_post_features_tfidf_256.csv")

print("done")
