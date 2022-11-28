#import dataFiles
import pandas as pd
colsToKeep = ["author", "date", "post"]

df = pd.read_csv("data/depression_post_features_tfidf_256 (1).csv")
print(df.head())
smallDF =df[colsToKeep]
smallDF.to_csv("simpfiedData/depression_post.csv")