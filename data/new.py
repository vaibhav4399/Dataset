import pandas as pd
import numpy as np

# import multiprocessing as mp

data = pd.read_csv("data5.csv")

d = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
     7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

n = 0
kharif = 0.0
rabi = 0.0

for i in range(len(data)):

    if int(data.loc[i, "Date"][:4]) > 1996 and int(data.loc[i, "Date"][:4]) < 2011:

        mon = int(data.loc[i, "Date"][5:7])
        data.loc[i, d.get(mon)] = data.loc[i, "Temperature"]

        if mon >= 5 and mon <= 10:
            kharif += data.loc[i, "Temperature"]
        else:
            rabi += data.loc[i, "Temperature"]

        if mon == 12:
            data.loc[i, "Kharif"] = kharif
            data.loc[i, "Rabi"] = rabi
            kharif = 0.0
            rabi = 0.0

        print(i)


data.to_csv("newdata5.csv", index=False)
print("Done")
