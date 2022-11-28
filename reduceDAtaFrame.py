import pandas as pd
import simpDataSets
import numpy as np
from sklearn.model_selection import train_test_split

jokes = simpDataSets.jokes_2018()

msk = np.random.rand(len(jokes)) < 0.2

test = jokes[msk]

print("old len", len(jokes))
print("new len", len(test))
print(test)
