import pandas as pd
import numpy as np

data = pd.read_csv("testdata.csv")

for i in range(len(data)):
    if pd.isnull(data.Yield[i]):
        print(i)
