import pandas as pd
import numpy as np

data = pd.read_csv("testdata2.csv")
data2 = pd.read_csv("newdata5.csv")


for i in range(len(data)):

    year = data.Year[i]
    # print(data2.Date.str[0:4].int == 1796)
    m = np.where(str(data2.Date)[:4] == 1804)[0]
    if len(m) > 0:
        print(m)
        break
