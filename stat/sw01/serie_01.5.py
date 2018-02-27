#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:28:06 2018

@author: Christopher
"""

from pandas import Series, DataFrame 
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

geysir = pd.read_table(r"geysir.dat", sep=" ", index_col=0)
geysir.head()
plt.subplot(221)
geysir["Zeitspanne"].plot(kind="hist", edgecolor="white")
plt.xlabel("10 Klassen")

plt.subplot(222)
geysir["Zeitspanne"].plot(kind="hist", bins=20,edgecolor="white")
plt.xlabel("20 Klassen")

plt.subplot(223)
geysir["Zeitspanne"].plot(kind="hist", bins=20, edgecolor="black")
plt.xlabel("20 Klassen")

plt.subplot(223) 
geysir["Zeitspanne"].plot(kind="hist", bins=np.arange(41,107,11), edgecolor="black") 
plt.xlabel("Klassengrenzen 41, 52 , 63, 74 , 85, 96")
plt.show()

print("Zwischen 40 und 60 Minuten und um 70 Minuten treten häufiger Ausbrüche auf.")

plt.subplot(221)
geysir["Eruptionsdauer"].plot(kind="hist", bins=5, edgecolor="white")
plt.subplot(222)
geysir["Eruptionsdauer"].plot(kind="hist", bins=10, edgecolor="white")
plt.subplot(223)
geysir["Eruptionsdauer"].plot(kind="hist", bins=20, edgecolor="white")
plt.subplot(224)
geysir["Eruptionsdauer"].plot(kind="hist", bins=30, edgecolor="white")

plt.show()

plt.subplot(221)
geysir["Eruptionsdauer"].plot(kind="hist", normed=True, cumulative=True, edgecolor="white")