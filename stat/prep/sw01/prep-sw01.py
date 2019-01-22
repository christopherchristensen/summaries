#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:17:10 2019

@author: christopher
"""

from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv(r"child.csv", sep=",", index_col=0)

dimension = data.shape
data.describe()
data.index

data.sort_values(by='Drunkenness', ascending=False)['Drunkenness'].head()
data.sort_values(by='Drunkenness', ascending=False)['Drunkenness'].max()

data.nsmallest(1, 'Infant.mortality')['Infant.mortality']
data.loc[data['Physical.activity'] < data['Physical.activity'].mean(), ['Physical.activity']]
data['Physical.activity'].mean()

"China" in data.index
"Netherlands" in data.index



# 1.2

data = pd.read_table(r"./d.fuel.dat", sep=",", index_col=0)
data.describe()
data.head()
data.sort_values(by='type', ascending=True).head()
data.loc[5,:]
data.head()
data.loc[1:5, :]

data['mpg'].mean() # 24.5833333
data.loc[7:22, 'mpg'].mean() # 27.75

data['t_kml'] = data['mpg'] * 0.42514
data['t_kg'] = data['weight'] * 3.785411784
data.describe()

data.mean()['t_kml'] # 10.4515
data.mean()['t_kg']  # 10980.8487

data.loc[:, 't_kml':'t_kg'].mean()
data.columns


# 1.3

data = Series([2.1,2.4,2.8,3.1,4.2,4.9,5.1,6.0,6.4,
               7.3,10.8,12.5,13.0,13.7,14.8,17.6,19.6, 
               23.0,25.0,35.2,39.6])

data.describe()
sum_x1 = data.sum() # 269.1
sum_x2 = (data*data).sum() # 5729.27

data.describe() # 12.8143, 10.6793
mean = data.sum() / data.size
std = np.sqrt((1/(data.size - 1)) * ((data - data.mean())**2).sum())


sorted = (data.sort_values(axis=0))
middle = np.round(sorted.size * 0.5 + 0.5) - 1
median = data.loc[middle]

mean1   = data.mean()
std1    = data.std()
median1 = data.median()

q_75 = np.round(data.size * 0.7 + 0.5) - 1
q_75 = data.loc[q_75]

q1_75 = data.quantile(q=0.7)

z_i = (data - data.mean()) / data.std()
z_i.mean()
z_i.std()


# 1.5

geysir = pd.read_table(r"./geysir.dat", delim_whitespace=True)
geysir.head()
geysir.describe()


plt.subplot(221)
geysir["Zeitspanne"].plot(kind="hist", bins=10, edgecolor="yellow")
plt.xlabel("10 Klassen")


plt.subplot(222)
geysir["Zeitspanne"].plot(kind="hist", bins=20, edgecolor="orange")
plt.xlabel("20 Klassen")

plt.subplot(223)
geysir["Zeitspanne"].plot(kind="hist", bins=np.arange(41, 107, 11), edgecolor="pink")
plt.xlabel("np.arrange(41,107,11)")

plt.subplots_adjust(wspace=0.3, hspace=0.5)

plt.show() # Es fällt auf, dass im letzten Histogram viel Information verloren geht


plt.subplot(221)
geysir["Eruptionsdauer"].plot(kind="hist", bins=10, edgecolor="yellow")
plt.xlabel("10 Klassen")


plt.subplot(222)
geysir["Eruptionsdauer"].plot(kind="hist", bins=20, edgecolor="orange")
plt.xlabel("20 Klassen")

plt.subplot(223)
geysir["Eruptionsdauer"].plot(kind="hist", bins=np.arange(41, 107, 11), edgecolor="pink")
plt.xlabel("np.arrange(41,107,11)")

plt.subplots_adjust(wspace=0.3, hspace=0.5)


plt.show() # Es fällt auf, dass im letzten Histogram viel Information verloren geht

np.corrcoef(geysir["Eruptionsdauer"], geysir["Zeitspanne"])
# Man könnte beinahe meinen die Werte korrelieren


geysir["Eruptionsdauer"].plot(kind="hist", density=True, cumulative=True)
geysir.head()

# 18.6916%
geysir["Eruptionsdauer"].loc[geysir["Eruptionsdauer"] < 2].size / geysir["Eruptionsdauer"].size
# 4 min
geysir["Eruptionsdauer"].sort_values().quantile(q=0.6)