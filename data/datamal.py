import pandas as pd
import re
import numpy as np

data = pd.read_csv("mydata2.csv")
data2 = pd.read_csv("imd_district_wise_rainfalldata_2004_2010.csv")
data3 = pd.read_csv("india___monthly_rainfall_data___1901_to_2002.csv")

dic = {"kharif": 1, "rabi": 0}

print("checking....")
for i in range(len(data)):
    if pd.isnull(data.Rainfall[i]):
        state = data.State[i].strip().lower()
        district = data.District[i].strip().lower()
        year = data.Year[i]
        season = data.Season[i].strip().lower()

        m = np.where((data2.State.str.strip().str.lower() == state) & (
            data2.District.str.strip().str.lower() == district) & (data2.Year == year))[0]

        n = np.where((data3.State.str.strip().str.lower() == state) & (
            data3.District.str.strip().str.lower() == district) & (data3.Year == year))[0]
        print(m)
        if len(m) > 0:
            a = data2.loc[m[0]].values[-1:-3:-1]
            if season == "kharif" or season == "rabi":
                data.loc[i, "Rainfall"] = a[dic[season]]
            print(m)
            exit()

        if len(n) > 0:
            a = data3.loc[n[0]].values[-1:-3:-1]
            if season == "kharif" or season == "rabi":
                data.loc[i, "Rainfall"] = a[dic[season]]
        print(i)

print("Deletiing Null values...")
for i in range(len(data)):
    if pd.isnull(data.Rainfall[i]):
        data.drop(i, inplace=True)
    print(i)

data.to_csv("testdata2.csv")
print("done")
