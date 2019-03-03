#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:53:18 2019

@author: christopher
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series


# =============================================================================
# 2.1
# =============================================================================
df1 = Series([4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1])


mean1   = df1.mean()
median1 = df1.median()

# Alle Werte unter und über dem Median können
# verändert werden ohne dass sich der Median verändert,
# solange diese nicht gerade die mittlere(n) (zwei) Beobachtung(en) entspricht.
df2 = Series([4.2, 4.0, 6.0, 4.5, 4.8, 3.9, 6.0, 3.4, 5.9, 6, 4, 3.7, 6, 6.0, 4.5, 3.6, 6, 6, 3.8, 3.3, 6.0, 4.2, 6.0, 6.0])
mean2   = df2.mean()
median2 = df2.median()


plt.subplot(221)

df1.plot(kind="hist", bins=8, edgecolor="black")
plt.title("Histogramm Original")

plt.subplot(222)
df1.plot(kind="box")
plt.title("Boxplot Original")

plt.subplot(223)

df2.plot(kind="hist", bins=8, edgecolor="black")
plt.title("Histogramm Verändert")

plt.subplot(224)
df2.plot(kind="box")
plt.title("Boxplot Verändert")

plt.tight_layout()
plt.show()


# =============================================================================
# 2.2
# =============================================================================
schlamm = pd.read_table('./data/klaerschlamm.dat', sep=' ', index_col=0)
schlamm = schlamm.drop("Labor", 1)
schlamm.head()

schlamm.describe()
schlamm.plot(kind="box")


schlamm_centered = schlamm - schlamm.median()
schlamm_centered.T.plot(kind="box")



# =============================================================================
# 2.4
# =============================================================================
hubble = pd.read_table("./data/hubble.txt", sep=" ")

b, a = np.polyfit(x=hubble["distance"], y=hubble["recession.velocity"], deg=1)

x = np.linspace(hubble["distance"].min(), hubble["distance"].max())
y = b * x + a

hubble.plot(kind="scatter", x="distance", y="recession.velocity")
plt.plot(x, y, c="orange")

plt.show()

hubble.corr().iloc[0,1]

# =============================================================================
# 2.5
# =============================================================================
income = pd.read_table(r"./data/income.dat", sep=" ")
income.describe()

b, a = np.polyfit(x=income["Educ"], y=income["Income2005"], deg=1)
x = np.linspace(income["Educ"].min(), income["Educ"].max())

income.plot(kind="scatter", x="Educ", y="Income2005")
plt.plot(x, a + b*x, c="orange")
plt.show()

income.corr()

# Fast keine Korrelation, was man auch am Plot erkennen kann


b, a = np.polyfit(income["AFQT"], income["Income2005"], deg=1)
x = np.linspace(income["AFQT"].min(), income["AFQT"].max())

income.plot(kind="scatter", x="AFQT", y="Income2005")
plt.plot(x, a + b * x, c="orange")

income.corr()

plt.show()

# Bei Extrapolation ist immer Vorsicht geboten

# =============================================================================
# 2.6
# =============================================================================
x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]) 
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]) 
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]) 
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])


df = DataFrame({
    "x": [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    "y1": [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
    "y2": [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
    "y3": [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
    "x4": [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
    "y4": [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
})


plt.subplot(221)
b_1, a_1 = np.polyfit(df["x"], df["y1"], deg=1)
x_1 = np.linspace(0, df["x"].max())

df.plot(kind="scatter", x="x", y="y1")
plt.plot(x_1, a_1 + b_1 * x_1, c="orange")


plt.subplot(222)

b_2, a_2 = np.polyfit(df["x"], df["y2"], deg=1)
x_2 = np.linspace(0, df["x"].max())
df.plot(kind="scatter", x="x", y="y2")
plt.plot(x_2, a_2 + b_2 * x_2, c="orange")


plt.subplot(223)

b_3, a_3 = np.polyfit(df["x"], df["y3"], deg=1)
x_3 = np.linspace(0, df["x"].max())
df.plot(kind="scatter", x="x", y="y3")
plt.plot(x_3, a_3 + b_3 * x_3, c="orange")

plt.subplot(224)

b_4, a_4 = np.polyfit(df["x4"], df["y4"], deg=1)
x_4 = np.linspace(0, df["y4"].max())
df.plot(kind="scatter", x="x4", y="y4")
plt.plot(x_4, a_4 + b_4 * x_4, c="orange")

plt.show()

np.corrcoef(df)

# =============================================================================
# 2.7
# =============================================================================
data = pd.read_csv("./data/child.csv", sep=",", index_col=0)

data.describe()
data.mean()
data.median()

# Check if there are nan's in data
data.isnull().values.any()
cleanedList = data.dropna()
cleanedList.isnull().values.any()

cleanedList2 = data.dropna(thresh=(data.index.size-1), axis=1)
filledList = data.fillna(method='bfill', axis='rows')

# Ist das nicht ein wenig ungünstig für z.B. Canada / Overcrowding