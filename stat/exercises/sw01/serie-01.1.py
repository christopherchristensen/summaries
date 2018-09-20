#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:48:49 2018

@author: christopher j. christensen
"""

# AUFGABE 1.1

##################################################

print("Hello STAT-Friends!")

##################################################
## Einführung Python

a = 3
b = 4

a + b

##################################################

a, b = 3, 4

a + b

##################################################

import numpy as np

np.sqrt(2)

x = np.array([1, 4, -3, 5, 9])

x

3 * x

x * x

np.linspace(start=1, stop=5, num=50)

np.arange(start=1, stop=5, step=0.75)

np.arange(9)

##################################################

import pandas as pd
from pandas import Series, DataFrame

temp_luz = Series([1, 5, 9, 15, 20, 25, 25])

temp_luz

temp_luz[3]

temp_luz = Series(
        [1, 5, 9, 15, 20, 25, 25],
        index=("jan", "feb", "mar", "apr", "may", "jun", "jul")
        )

temp_luz

temp_luz["mar"]

temp_luz.index

temp_luz.mean()

temp = DataFrame({
        "Luzern": ([1, 5, 9, 15, 20, 25, 25]),
        "Basel": ([3, 4, 12, 16, 18, 23, 32]),
        "Zuerich": ([8, 6, 10, 17, 23, 22, 24])},
        index=["jan", "feb", "mar", "apr", "may", "jun", "jul"]
)

# Dataframe ausgeben
temp

# Spaltennamen abfragen
temp.columns

# Durchschnittliche Temperaturen in den einzelnen Städten
temp.mean()

# Durchschnittliche Temperaturen in den einzelnen Monaten aller Städte
temp.mean(axis=1)

# Mindesttemperaturen der einzelnen Monaten
temp.min(axis=1)

# Eine einzelne Spalte betrachten
temp["Luzern"]

# Selbe Abfrage wie oben einfach in Matrizenform
# Der alleinstehende : als 1. Argument soll andeuten, 
# dass alle Zeilen gemeint sind.
# Der : als 1. Argument hat die Bedeutung „von ... bis”
temp.loc[:, "Luzern"]

# Temperaturen von Mai bis Juli in Luzern
temp.loc["may":"jul", "Luzern"]

# Auswahl von Zeilen und Spalten
temp.loc[["may", "jan"], ["Luzern", "Basel"]]

# Einzelner Wert abfragen
temp.loc["may", "Luzern"]


##################################################

# AUFGABE 1.2

##################################################

from pandas import Series,DataFrame 
import pandas as pd

# Datei einlesen und in Variable (data) speichern
data = pd.read_csv(r"./child.csv", sep=",", index_col=0)

## TODO...

##################################################

# AUFGABE 1.3

##################################################

import pandas as pd
from pandas import DataFrame, Series
fuel = pd.read_table(r"d.fuel.dat", sep=",", index_col=0)


##################################################

# AUFGABE 1.4

##################################################

import pandas as pd
from pandas import DataFrame, Series
fuel = pd.read_table(r"*d.fuel.dat", sep=",", index_col=0)