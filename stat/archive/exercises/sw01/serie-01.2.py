#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:46:45 2018

@author: christopher
"""

##################################################

# AUFGABE 1.1

##################################################

from pandas import Series,DataFrame 
import pandas as pd

# Datei einlesen und in Variable (data) speichern
data = pd.read_csv(r"./child.csv", sep=",", index_col=0)

# Dimension der Daten
data.shape

# Daten beschreiben
data.describe()

# Zeilen
data.index

# Sortieren (nur 5 ersten Resultate => head(5))
data.sort_values(by=["Drunkenness"], ascending=False)["Drunkenness"].head(5)

# Filtern nach kleinsten Einträgen
data.nsmallest(1, ["Infant.mortality"])["Infant.mortality"]

# Nach Schlüssel filtern
data.loc[["Switzerland"], ["Infant.mortality"]]

# Filtern nach Bedingung
data.loc[data["Physical.activity"] < data["Physical.activity"].mean()]["Physical.activity"]


##################################################

# AUFGABE 1.2

##################################################

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

# Datei einlesen und in Variable (fuel) speichern
fuel = pd.read_table(r"d.fuel.dat", sep=",", index_col=0)

# Daten beschreiben
fuel.describe

# 5. Eintrag lesen
fuel.loc[5]

# 1. bis 5. Eintrag lesen
fuel.head(5)

# 1. bis 5. Eintrag lesen (Alternative)
fuel.loc[1:5, :]

# Mittelwert der Reichweite aller Autos in Miles/Gallon
fuel["mpg"].mean()

# Mittelwert der Reichweite der Autos 7 bis 22
fuel.loc[7:22, :]["mpg"].mean()

# Neuer Vektor mit allen Reichweiten in km/l
t_kml = fuel["mpg"] * 0,425144

# Neuer Vektor mit allen Gewichten
t_kg = fuel["weight"] * 0.45359

# Daten beschreiben
t_kg.describe

# Mittelwert der Gewichte
# Daten beschreiben
t_kg.mean()


##################################################

# AUFGABE 1.3

##################################################


# Series erstellen
data = pd.Series([
        2.1,2.4,2.8,3.1,4.2,4.9,5.1,6.0,6.4,7.3,10.8,12.5,
        13.0,13.7,14.8,17.6,19.6, 23.0,25.0,35.2,39.6
        ])

# Summe der Einträge einer Series berechnen
data.sum()

# Mittelwert ohne pandas berechnen
mittelwert = data.sum() / data.size
varianz = 1 / (data.size - 1) * ((data - mittelwert)**2).sum()
standardabweichung = np.sqrt(varianz)

# Mittelwert und Standardabweichung ausgeben
mittelwert
varianz
standardabweichung

# Median ohne pandas berechnen
data.sort_values(ascending=False)
mittlererWert = int(np.round(data.size / 2))
mittlererWert
data[mittlererWert]

# Median, Varianz und Standardabweichung mit pandas ausgeben
data.mean()
data.var()
data.std()

# 75%-Quantil ausgeben
data.quantile(q=0.75, interpolation="midpoint")

# Arithmetische Mittel der standardisierten Variablen
((data - data.mean()) / data.std()).mean()


##################################################

# AUFGABE 1.4

##################################################

a = 3
b = 1
c = 2


##################################################

# AUFGABE 1.5

##################################################

from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

# Daten von Datei laden
geysir = pd.read_table(r"geysir.dat", sep=" ", index_col=0)
 
# Überprüfen
geysir.head()

# Plot ohne Daten
plt.subplot(221)

# Histogramm der geysir Daten
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
                            bins=np.arange(41,107,11),
                            edgecolor="black") 

plt.xlabel("Klassengrenzen 41, 52 , 63, 74 , 85, 96")

plt.show()

# Was fällt auf?
#-----------------
# Mit 20 Klassen sieht man zwei Peaks und ein Loch zwischen den Werten
# 60 und 80. Bei 5 Klassen gehen deutlich mehr Informationen verloren

# Histogramm der Eruptionsdauer
plt.subplot(221)
geysir["Eruptionsdauer"].plot(kind="hist", edgecolor="black")

plt.subplot(222)
geysir["Eruptionsdauer"].plot(kind="hist", bins=20, edgecolor="black")


# Was fällt auf?
#-----------------
# Keine Ahnung

geysir["Eruptionsdauer"].plot(kind="hist", normed=True,
                                cumulative=True)
 