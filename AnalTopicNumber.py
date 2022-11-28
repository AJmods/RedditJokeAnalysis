import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits import mplot3d
import numpy as np

#mpl.use("Qt5Agg")

df = pd.read_csv("ModifedData/doms.csv")

jokes = []
percent = []
topics = []
i = 0
for row in df.iterrows():
    i += 1
    # print(row)
    jokes.append(row[1]['Text'])
    percent.append(row[1]['Topic_Perc_Contrib'])
    topics.append(row[1]['Dominant_Topic'])
    if i % 3000 == 0:
        print("on i = ", i)
        #break

order = np.argsort(topics)
jokes = list(np.array([len(joke) for joke in jokes])[order])
percent = list(np.array(percent)[order])
topics = list(np.array(topics)[order])

fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
ax = fig.gca(projection="3d")
#yline = #[len(joke) for joke in jokes]
#xline = topics

currentTopic = 0
while topics:
    x = []
    y = []
    z = []
    currentTopic = topics[-1]
    print("on topic", currentTopic)
    if currentTopic != 27:
        while currentTopic == topics[-1]:
            x.append(percent.pop())
            y.append(jokes.pop())
            z.append(topics.pop())
            if not topics:
                break

        ax.scatter(x, z, y, label=currentTopic)
    else:
        while topics[-1] == 27:
            topics.pop()
# xline, yline = np.meshgrid(xline, yline)

# zline = np.sin(xline)
# ax.scatter(xline, yline, zline, marker='o')
# ax.plot_surface(xline, yline, zline, cmap=cm.coolwarm,linewidth=0, antialiased=False)
# plt.scatter(percent, [len(joke) for joke in jokes], s=1)\
# plt.xlabel("Percent of being associated to topic")
# plt.ylabel("Word Count")

ax.set_xlabel("Percent related to topic")
ax.set_ylabel("Topic Number")
ax.set_zlabel("Word Count")

ax.set_zlim(0, 3000)

plt.legend()
# ax.set_aspect('auto')
plt.show()
