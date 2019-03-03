#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:44:38 2019

@author: christopher
"""

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from pandas import DataFrame


# --- 12.1

pw_electric = pd.read_csv('PW_electric.csv', sep=',', skiprows=2, header=0,
encoding = "utf-8", index_col=0)
pw_electric.head()
pw_electric_luzern = DataFrame(pw_electric.ix["Luzern",1:]) 
pw_electric_luzern
pw_electric_luzern["Year"] = pd.DatetimeIndex(pw_electric_luzern.index)

pw_electric_luzern.set_index("Year", inplace=True) 
pw_electric_luzern.plot()
plt.xlabel("Jahr")
plt.ylabel("Anzahl Elektro-Autos Luzern") 
plt.show()

pw_electric_zurich = DataFrame(pw_electric.ix["Zürich",1:]) 
pw_electric_zurich
pw_electric_zurich["Jahr"] = pd.DatetimeIndex(pw_electric_zurich.index)

pw_electric_zurich.set_index("Jahr", inplace=True) 
pw_electric_zurich.plot()
plt.xlabel("Jahr")
plt.ylabel("Anzahl Elektro-Autos Zurich") 
plt.show()



# Relativer Zuwachs in Luzern
pw_electric_luzern["rel"] = np.log(pw_electric_luzern.astype('float')) - np.log(pw_electric_luzern.shift(1).astype('float'))


# Relativer Zuwachs in Zuerich
pw_electric_zurich["rel"] = np.log(pw_electric_zurich.astype('float')) - np.log(pw_electric_zurich.shift(1).astype('float'))


pw_rel = pd.DataFrame({
        "Luzern" : pd.Series(pw_electric_luzern["rel"]), 
        "Zürich" : pd.Series(pw_electric_zurich["rel"])
})

pw_rel.plot()


# --- 12.2

AusBeer = pd.read_csv("AustralianBeer.csv",sep=";",header=0) 
AusBeer.head()

AusBeer["Quarter"] = pd.DatetimeIndex(AusBeer["Quarter"]) 
AusBeer.set_index("Quarter", inplace=True) 
AusBeer.columns=["Megalitres"]
AusBeer



AusBeer.plot() 

plt.ylabel("Megalitres Beer")


AusBeer.describe()

AusBeer.resample("A").mean().plot() 
AusBeer['quarter'] = AusBeer.index.quarter 
AusBeer.boxplot(by="quarter")

plt.ylabel("Megalitres Beer") 
plt.xlabel("Year")
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose 
seasonal_decompose(AusBeer, model="additive", freq=4).plot()


from stldecompose import decompose
AusBeer_stl = decompose(AusBeer["Megalitres"], period=4) 
AusBeer_stl.plot();



# --- 12.3

Electricity = pd.read_csv("AustralianElectricity.csv", sep=";", header=0)

Electricity.head()

Electricity["Quarter"] = pd.DatetimeIndex(Electricity["Quarter"]) 
Electricity.set_index("Quarter", inplace=True) 
Electricity.columns=["Electricity production Australia"] 
Electricity.head()
Electricity.plot() 
plt.ylabel("Million Kilowatthours")


def boxcox(x,lambd):
    return np.log(x) if (lambd==0) else (x**lambd-1)/lambd

# replace "yourSeries" by the name of your series
Electricity_tr = boxcox(Electricity, 0) 
Electricity_tr.plot()
plt.show()


from statsmodels.tsa.seasonal import seasonal_decompose 
seasonal_decompose(Electricity_tr, model="additive", freq=4).plot() 
plt.show()


E_stl = decompose(Electricity_tr, period=4)
E_stl.plot()