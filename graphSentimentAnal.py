import simpDataSets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.dates as mdates

percent = 1

print('loading sentiment dataset')
deprSentiment = simpDataSets.all_jokes_sentiment()
print('loading joke dataset')
allJokes = simpDataSets.allJokeDatesets()

for i in range(len(allJokes)):
    msk = np.random.rand(len(allJokes[i])) < percent

    allJokes[i] = allJokes[i][msk]
    df = pd.DataFrame(deprSentiment[i])
    deprSentiment[i] = df[msk]
averages = []
# print(deprSentiment[0][0].keys())
pos = []
neu = []
neg = []
comp = []
date = []
print("adding values to list")

for j in range(len(deprSentiment)):
    print("on dataset ", j)
    for i in range(len(deprSentiment[j])):
        pos.append(deprSentiment[j].iloc[i]['pos'])
        neu.append(deprSentiment[j].iloc[i]['neu'])
        neg.append(deprSentiment[j].iloc[i]['neg'])
        comp.append(deprSentiment[j].iloc[i]['compound'])
        date.append(allJokes[j].iloc[i]['date'])
        if i % 3000 == 0:
            print("on idx ",i)

print("making graph")
# xVal = [dt.datetime.strptime(d, '%Y/%m/%d').date() for d in date]
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=int(len(date) / 3)))

# xVal = np.arange(len(pos))
# plt.scatter(xVal, pos, label="positive")
# plt.scatter(xVal, neu, label="neutral")
# plt.scatter(xVal, neg, label="negative")
plt.hist(neu, bins=50)
#plt.scatter(xVal, comp, label="compond", s=.1)
# plt.gcf().autofmt_xdate()

plt.xlabel("Score")
plt.ylabel("Freqency")
plt.title("Joke Neutral Scores")
plt.legend()
plt.show()
