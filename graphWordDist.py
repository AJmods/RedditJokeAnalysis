import pandas as pd
import matplotlib.pyplot as plt

topic = 25
df = pd.read_csv(f"ModifedData/TopicsAlldoms.csv") #/topic{topic}.csv")

lenWords = []
longs = []
words = 0
for joke in df.iterrows():
    lenWord = len(joke[1]['Text'])
    if lenWord >= 0:
        for word in joke[1]['Text'].split(" "):
            if word == "would":
                words += 1
        longs.append(lenWord)
    else:
        lenWords.append(lenWord)

print(f"W COunt {words}")
# for i in range(200):
#     if i in lenWords:
#         pass
#     else:
#         print("No jokes of len ", i)
print("number of jokes over some words")
print(len(longs))
print(len(longs) / len(lenWords))
plt.hist(lenWords, bins=1000)
plt.xlabel("Word Frequency")
plt.ylabel("Word Count")
plt.title(f"Word Count Vs Frequency for topic {topic}")
plt.show()