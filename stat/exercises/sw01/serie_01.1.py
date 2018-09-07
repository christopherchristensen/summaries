# -*- coding: utf-8 -*-
"""
Spyder Editor

My First Playground
"""

import numpy as np
from numpy import sqrt
"from numpy import *"
import pandas as pd
from pandas import Series, DataFrame

print('Hello world')

a = 3
b = 4

a + b

a, b = 3, 4
a + b

"-------------"

print(np.sqrt(2))
print(sqrt(2))
print('')

x = np.array([2, 1, 4, 5, -8])
print(x)
print(3*x)
print(x*x)
print('')

x = np.linspace(start=1, stop=2, num=4)
print(x)
print('')

y = np.arange(start=1, stop=7, step=.6)
print(y)
print('')

z = np.arange(1, 9) 
print(z)
print('')

w = np.arange(9)
print(w)
print('')

"-------------"

temp_luz = Series([1,5,9,15,20,25,25])
print("Series = ")
print(temp_luz)
print("")
print("temp_luz[2] = "+str(temp_luz[2]))
print("")

temp_luz = Series(
        [1,5,9,15,20,25,25], 
        index=("jan","feb", "mar", "apr", "mai", "jun", "jul")
        )
print("Series mit eigenem Index = ")
print(temp_luz)
print("")
print("März = "+str(temp_luz["mar"]))
print("")
print("Index von Series: ")
print(temp_luz.index)
print("")
print("temp_luz.mean() = "+str(temp_luz.mean()))
print("")
print("temp_luz.size = "+str(temp_luz.size))
print("")
print("-----------------")
print("")
temp = DataFrame({
"Luzern": ([1,5,9,15,20,25,25]),
"Basel": ([3,4,12,16,18,23,32]),
"Zuerich": ([8,6,10,17,23,22,24])}, index=["jan","feb","mar","apr","mai","jun","jul"]
)
print("")
print("Temperaturen von Jan - Jul:")
print("")
print(temp)
print("")
print("Die Spaltennamen: ")
print("")
print(temp.columns)
print("")
print("Die Mittelwerte der Temperaturen pro Region: ")
print("")
print(temp.mean())
print("")
print("Die Mittelwerte der Temperaturen pro Monat: ")
print("")
print(temp.mean(axis=1))
print("")
print("Die Mindesttemperaturen pro Monat: ")
print("")
print(temp.min(axis=1))
print("")
print("Die Temperaturen pro Monat in Luzern: ")
print("")
print(temp["Luzern"])
print("")
print("Die Temperaturen pro Monat in Luzern in Matrizenform: ")
print("")
print(temp.loc[:,"Luzern"])
print("")
print("Die Temperaturen bestimmter Monate in Luzern in Matrizenform: ")
print("")
print(temp.loc["mai":"jul","Luzern"])
print("")
print(temp.loc[["mai","jul"],["Basel","Luzern"]])
print("")
print(temp.loc["jul","Basel"])
print("")
print("")
print("------------------")

