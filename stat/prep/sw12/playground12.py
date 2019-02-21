#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:52:20 2019

@author: christopher
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

AirP = pd.read_csv("AirPassengers.csv") 
AirP.head()
AirP["TravelDate"] = pd.DatetimeIndex(AirP["TravelDate"]) 

AirP.head()

AirP.set_index("TravelDate", inplace=True)
AirP.head()
AirP.plot()
plt.xlabel("Reisedatum") 


AusBeer = pd.read_csv("AustralianBeer.csv",sep=";",header=0)
AusEl = pd.read_csv("AustralianElectricity.csv",sep=";")
AusBeer.head()
AusBeer1 = AusBeer.copy()

AusBeer1["Quarter"] = pd.DatetimeIndex(AusBeer["Quarter"])
AusBeer1.set_index("Quarter", inplace=True)

AusBeer1.describe()

AusBeer1.loc["1980-9":"2000-3",:].plot()



Aussie = AusBeer.copy()
# Hier wird der Datensatz um eine Spalte erweitert
Aussie["kilowatt"] = AusEl["kilowatt"] 
Aussie["Quarter"]=pd.DatetimeIndex(Aussie["Quarter"])
Aussie.set_index("Quarter", inplace=True) 
Aussie.plot(subplots=True)
plt.show()

def boxcox(x,lambd):
    return np.log(x) if (lambd==0) \
    else (x**lambd-1)/lambd
    
AirP["l_2"] = boxcox(AirP["Passengers"],2) 
AirP["l_0"] = boxcox(AirP["Passengers"],0) 
AirP["l_-05"] = boxcox(AirP["Passengers"],-.5)


plt.subplot(221) 
AirP["Passengers"].plot() 
plt.title("Original") 
plt.xlabel("")


plt.subplot(222) 
AirP["l_-05"].plot() 
plt.title("lambda=-0.5") 
plt.xlabel("")

plt.subplot(223) 
AirP["l_2"].plot() 
plt.title("lambda=2") 
plt.xlabel("")

plt.subplot(224) 
AirP["l_0"].plot() 
plt.title("lambda=0") 
plt.xlabel("")
plt.tight_layout()
plt.show()




AirP["s_4"] = AirP["Passengers"].shift(4)
AirP["s_-5"] = AirP["Passengers"].shift(-5)
AirP["Passengers"].plot()
AirP["s_4"].plot()
AirP["s_-5"].plot() 
plt.legend(["Original","zurueckverschoben","vorverschoben"])
plt.show()

AirQ = pd.read_csv("AirQualityUCI.csv",sep=";",decimal=",")
AirQ1 = AirQ.copy()
  

AirQ1 = AirQ.copy()

#pandas kennt das Zeitformat in der Tabelle nicht: 
#Punkt muss durch - ersetzt werden
AirQ1["Time"] = AirQ1["Time"].str.replace(".","-")
AirQ1["Date"] = pd.DatetimeIndex(AirQ1["Date"]+" "+AirQ1["Time"]) 
AirQ1.set_index("Date", inplace=True)
# Einige Wert der Temperatur sind -200. Diese Zeilen werden weggelassen
AirQ1 = AirQ1[AirQ1["T"] > -20] 
AirQ1["T"].plot()
plt.show()


# Fokus auf 20 Tage
AirQ4 = AirQ1.loc["2004-3-10":"2004-3-30","T"] 
AirQ4.plot()


AirQ1.boxplot("T",by="Time") 
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

from pandas.plotting import lag_plot

plt.subplot(121)
lag_plot(AirQ4) 
plt.subplot(122)
lag_plot(AirQ4, 10) 

plt.tight_layout()
plt.show()



AirP["Trend"] = AirP["Passengers"].rolling(window=12).mean()
AirP["Passengers"].plot()
AirP["Trend"].plot() 
plt.legend(["Daten","Trend"]) 
plt.show()

AirP["Season"] = AirP["Passengers"]-AirP["Trend"]
AirP["Season"].plot() 
plt.show()


# AirP[’Season’] wird in eine Matrix umgewandelt 
# mit den Monaten als Spalten (Jahre als Zeilen)
AirP2 = AirP["Season"].values.reshape((12,12))
# Entlang der Spalten (axis=0) wird der Mittelwert genommen
# nanmean bedeutet, die NaN werden ignoriert
ave = np.nanmean(AirP2,axis=0)
# Der Vektor ave wird verzwölfacht,
# damit er wieder die gleiche Länge hat, wie AirP[’Season’]
AirP["Season_ave"] = np.tile(A=ave, reps=12) 
AirP["Season_ave"].plot()
plt.show()


AirP["Residual"] = AirP["Season"]- AirP["Season_ave"] 
AirP["Residual"].plot()
plt.show()


from statsmodels.tsa.seasonal import seasonal_decompose 
seasonal_decompose(AirP["Passengers"], model="additive", freq=12).plot() 
plt.show()

seasonal_decompose(np.log(AirP["Passengers"]), model="add").resid.plot() 
plt.show()



import matplotlib.pyplot as plt 
import pandas as pd


AirP = pd.read_csv("./AirPassengers.csv") 

AirP.head()

AirP["TravelDate"] = pd.DatetimeIndex(AirP["TravelDate"])
AirP.set_index("TravelDate", inplace=True)
AirP.head()
AirP.plot()
plt.xlabel("Reisedatum") 
plt.ylabel("Anzahl Passagiere (in 1000)")
plt.show()

# Teilmenge von AirP
AirP.loc["1949-3":"1955-3"].plot()
plt.xlabel("Reisedatum 1949/3 bis 1955/3") 
plt.ylabel("Anzahl Passagiere (in 1000)")
plt.show()


AusBeer = pd.read_csv("./AustralianBeer.csv",sep=";",header=0)
AusBeer1 = AusBeer.copy() 
AusBeer1.head()

AusBeer1["Quarter"] = pd.DatetimeIndex(AusBeer1["Quarter"])
AusBeer1.set_index("Quarter", inplace=True)
AusBeer1.plot()
plt.show()

AusBeer1.describe()


AusBeer = pd.read_csv("./AustralianBeer.csv",sep=";",header=0) 
AusEl = pd.read_csv("./AustralianElectricity.csv",sep=";")

AusBeer1 = AusBeer.copy()
AusBeer1["kilowatt"] = AusEl["kilowatt"]

AusBeer1["Quarter"] = pd.DatetimeIndex(AusBeer1["Quarter"])
AusBeer1.set_index("Quarter", inplace=True)

AusBeer1.plot(subplots=True)

AirQ = pd.read_csv("./AirQualityUCI.csv", sep=";", decimal=",")
AirQ["Time"] = AirQ["Time"].str.replace(".","-")
AirQ["Date"] = pd.DatetimeIndex(AirQ["Date"]+" "+AirQ["Time"])
AirQ.set_index("Date", inplace=True)
AirQ1 = AirQ.copy()

AirQ2 = AirQ1.loc["2004-03-10":"2004-03-30"]
AirQ2 = AirQ2[AirQ2["T"] > -20]
AirQ2["T"].plot()

AirQ2.boxplot("T", by="Time")
plt.xticks(rotation=45)
plt.show()


from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np 

seasonal_decompose(np.log(AirP["Passengers"]), model="add", freq=12).resid.plot()