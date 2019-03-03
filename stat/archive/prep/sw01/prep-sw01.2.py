from pandas import Series, DataFrame 
import pandas as pd
import numpy as np


# --- 1.1
data = pd.read_csv(r"./child.csv", sep=",", index_col=0)

data.shape
data.describe()
data.index
data.columns

sortedData = data.sort_values(by="Drunkenness", ascending=False)
sortedData["Drunkenness"].head()

data.nsmallest(1, "Infant.mortality")
data["Infant.mortality"]["Switzerland"]

data.loc[data["Physical.activity"] < data["Physical.activity"].mean(), :]

"China" in data.index
"Netherlands" in data.index
"Drunkenness" in data.columns



# --- 1.2

fuel = pd.read_table(r"./d.fuel.dat", sep=",", index_col=0)
fuel.describe
fuel.loc[5]
fuel.loc[1:5]
fuel.mean()["mpg"]
fuel.loc[7:22].mean()["mpg"]

t_kml = fuel["mpg"] * 0.43
t_kml.describe
t_kg = fuel["weight"] * 0.45359 

t_kml.mean()
t_kg.mean()



# --- 1.3
ha = Series([2.1,2.4,2.8,3.1,4.2,4.9,5.1,6.0,6.4,7.3,10.8,12.5,13.0,13.7,14.8,17.6,19.6, 23.0,25.0,35.2,39.6])

ha_sum = ha.sum()
ha_sum_square = (ha**2).sum()
ha_mean = ha_sum / ha.size
ha_std = np.sqrt(((ha - ha_mean)**2).sum() / (ha.size-1))
ha_sorted = ha.sort_values(axis=0)
ha_median = ha_sorted[np.round(ha.size/2 + 0.5) - 1]
ha.mean()
ha.median()
ha.std()
ha.quantile(q=0.75, interpolation="midpoint")

z_i = (ha - ha.mean()) / ha.std()
z_i.mean()
z_i.std()