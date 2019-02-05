#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:20:40 2019

@author: christopher
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# --- 1.1
data = pd.read_csv(r"child.csv", sep=",", index_col=0)
data.shape
data.describe()
data.index
drunk = data.sort_values(by="Drunkenness", ascending=False)["Drunkenness"]
drunk.head()

"China" in data.index
"Netherlands" in data.index

data.columns
data.nsmallest(1, "Infant.mortality")["Infant.mortality"]

data.loc[data["Physical.activity"]<data["Physical.activity"].mean(), :].index


# --- 1.3
flaeche = Series([2.1,2.4,2.8,3.1,4.2,4.9,5.1,6.0,6.4,7.3,10.8,12.5,13.0,13.7,14.8,17.6,19.6, 23.0,25.0,35.2,39.6])

flaeche.size

flaeche.sum()
flaeche_mittel = flaeche.sum() / flaeche.size
flaeche_std = 0

for x in flaeche: 
    flaeche_std += (x - flaeche_mittel)**2
    
flaeche_std /= flaeche.size-1
flaeche_std = np.sqrt(flaeche_std)

flaeche_median = flaeche.sort_values()[np.round((flaeche.size / 2) + 0.5, 0) - 1]
flaeche.median()
flaeche.std()
flaeche.mean()

Z = (flaeche - flaeche_mittel) / flaeche.std()

    
Z_mittel = Z.mean()


# --- 1.5
geysir = pd.read_table(r"geysir.dat", sep=" ", index_col=0)

geysir.head()

plt.subplot(221)
geysir["Zeitspanne"].plot(kind="hist", edgecolor="black") 
plt.xlabel("10 Klassen")


plt.subplot(222) 
geysir["Zeitspanne"].plot(kind="hist",
                            bins=20,
                            edgecolor="black")

plt.xlabel("20 Klassen")


plt.subplot(223) 
geysir["Zeitspanne"].plot(kind="hist",
                            bins=np.arange(41,107,11), edgecolor="black") 

plt.xlabel("Klassengrenzen 41, 52 , 63, 74 , 85, 96")

plt.tight_layout()
plt.show()




plt.subplot(221)
geysir["Eruptionsdauer"].plot(kind="hist", edgecolor="black") 
plt.xlabel("10 Klassen")


plt.subplot(222) 
geysir["Eruptionsdauer"].plot(kind="hist",
                            bins=20,
                            edgecolor="black")

plt.xlabel("20 Klassen")


plt.subplot(223) 
geysir["Eruptionsdauer"].plot(kind="hist",
                            bins=np.arange(41,107,11), edgecolor="black") 

plt.xlabel("Klassengrenzen 41, 52 , 63, 74 , 85, 96")

plt.tight_layout()
plt.show()

geysir["Eruptionsdauer"].plot(kind="hist", normed=True,
                                cumulative=True)
 