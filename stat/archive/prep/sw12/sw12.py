#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 08:01:15 2019

@author: christopher
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame, Series
from statsmodels.tsa.seasonal import seasonal_decompose


# --- 12.1
pwe = pd.read_csv("./PW_electric.csv", 
                  sep=',', 
                  skiprows=2, 
                  header=0,
                  encoding = "utf-8", 
                  index_col=0);

pw_l = DataFrame(pwe.ix["Luzern", 1:])
pw_l["Year"] = pd.DatetimeIndex(pw_l.index)
pw_l.set_index("Year", inplace=True)

pw_l.plot()
plt.xlabel("Jahr")
plt.ylabel("Elektrofahrzeuge Luzern")
plt.show()




pw_z = DataFrame(pwe.ix["Zürich", 1:])
pw_z["Year"] = pd.DatetimeIndex(pw_z.index)
pw_z.set_index("Year", inplace=True)

pw_z.plot()
plt.xlabel("Jahr")
plt.ylabel("Elektrofahrzeuge Zürich")
plt.show()

                  

# Nur vergleichbar, wenn man relativen Zuwachs betrachtet
# Zürich hat ja absolut viel mehr Autos und viel grösseren Zuwachs in der Menge
rel_l = np.log(pw_l["Luzern"].astype('float')) - np.log(pw_l["Luzern"].shift(1).astype('float'))
rel_z = np.log(pw_z["Zürich"].astype('float')) - np.log(pw_z["Zürich"].shift(1).astype('float'))

rel = DataFrame({
        "Luzern": rel_l,
        "Zürich": rel_z
})

rel.plot()
plt.legend(["Luzern", "Zürich"])
plt.xlabel("Jahr")
plt.ylabel("relativer Zuwachs Elektrofahrzeuge")
plt.show()


# --- 12.2
AusBeer = pd.read_csv("./AustralianBeer.csv", sep=";")
AusBeer1 = AusBeer.copy()
AusBeer1["Quarter"] = pd.DatetimeIndex(AusBeer1["Quarter"])
AusBeer1.set_index("Quarter", inplace=True)

AusBeer1.plot()
plt.title("Yearly Beer Production Australia")
plt.xlabel("Year")
plt.ylabel("MegaLitres Produced")
plt.show()

# saisonale Effekte wurden entfernt
# man sieht nun den steigenden Trend sehr gut
# zwischen 1960 und 1975
AusBeer1.resample("A").mean().plot() 
AusBeer1.resample("A").mean().head() 
AusBeer1.resample("A").mean().describe() 
AusBeer1['quarter'] = AusBeer1.index.quarter 
AusBeer1.boxplot(by="quarter")
plt.tight_layout()
plt.show()

# Saisonale Effekte sind ziemlich stabil über
# dem Zeitraum verteilt (also => Varianz ungefähr konstant)
# Deswegen ist keine Transformation notwendig
# Das Residual sieht sehr zufällig aus, also ist bestätigt,
# dass eine Transformation nicht notwendig ist
seasonal_decompose(AusBeer1["megalitres"], model="additive", freq=4).plot()


from stldecompose import decompose

decompose(AusBeer1["megalitres"], period=4).plot()
decompose(AusBeer1["megalitres"], period=8).plot()
decompose(AusBeer1["megalitres"], period=1).plot()



# --- 12.3
ae = pd.read_csv("./AustralianElectricity.csv", sep=";")
ae1 = DataFrame(ae.copy())
ae1["Quarter"] = pd.DatetimeIndex(ae1["Quarter"])
ae1.set_index("Quarter", inplace=True)

ae1.plot()
plt.title("Australian Electricity")
plt.show()

def boxcox(x, lambd):
    return np.log(x) if (lambd == 0) \
        else (x**lambd - 1) / lambd
        
ae_l05 = boxcox(ae1, 5)


ae_l05.plot()
plt.title("Australian Electricity, Lamdba 5")
plt.show()

ae_l00_5 = boxcox(ae1, 0.5)
ae_l00_5.plot()
plt.title("Australian Electricity, Lambda 0.5")
plt.show()

ae_l01_3 = boxcox(ae1, 1.3)
ae_l01_3.plot()
plt.title("Australian Electricity, Lambda 1.3")
plt.show()


# die saisonalen Effekte werden zunehmend grösser
# deswegen ist eine Transformation sinnvoll
# man sieht einen steigenden Trend
# die Residuen haben zwischen 1959 und 1969 ein 
# erkennbares Muster
seasonal_decompose(ae1["kilowatt"], model="additive", freq=4).plot()

# Nach der Transformation ist kaum noch ein Muster erkennbar
seasonal_decompose(ae_l00_5["kilowatt"], model="additive", freq=4).plot()


decompose(ae_l00_5["kilowatt"], period=4).plot()