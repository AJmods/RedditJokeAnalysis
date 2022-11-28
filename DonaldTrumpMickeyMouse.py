import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ModifedData/Topics/topic14.csv")

mickey = 0
trump = 0
both = 0
none = 0
for row in df.iterrows():
    joke = row[1]['Text'].lower()
    words = joke.split(" ")
    compareWords = ["mickey", "mouse"]
    if compareWords[0] in words:
        if compareWords[1] in words:
            both += 1
        else:
            mickey += 1
    elif compareWords[1] in words:
        if compareWords[0] in words:
            both += 1
            # print(joke)
        else:
            trump += 1
    else:
        none += 1

plt.bar([compareWords[0],  compareWords[1]], [mickey+both, trump+both])
plt.title(f"Ocurances of {compareWords[0]} and { compareWords[1]} for Topic 14")
plt.ylabel("Joke Count")
plt.show()
