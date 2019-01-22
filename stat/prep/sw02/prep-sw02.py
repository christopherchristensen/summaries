#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:47:27 2019

@author: christopher
"""

# --- 2.2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


schlamm = pd.read_table(r"./klaerschlamm.dat", sep=" ")
schlamm.describe()
schlamm.head()
schlamm.drop("Labor", 1)
 

plt.subplot(221)
schlamm["Pr1"].plot(kind="box")
plt.subplot(222)
schlamm["Pr2"].plot(kind="box")
plt.subplot(223)
schlamm["Pr3"].plot(kind="box")
plt.subplot(224)
schlamm["Pr4"].plot(kind="box")

plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.show()


plt.subplot(221)
schlamm["Pr5"].plot(kind="box")
plt.subplot(222)
schlamm["Pr6"].plot(kind="box")
plt.subplot(223)
schlamm["Pr7"].plot(kind="box")
plt.subplot(224)
schlamm["Pr8"].plot(kind="box")

plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.show()


plt.subplot(221)
schlamm["Pr9"].plot(kind="box")

plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.show()


schlamm
schlamm_centered = schlamm.drop("Labor", 1) - schlamm.drop("Labor", 1).median()
schlamm_centered.T.plot(kind="box")


# --- 2.4

hubble = pd.read_table(r"hubble.txt", sep=" ")
hubble.describe()
hubble.loc[2:7, "distance"]



hubble.plot(kind="scatter", x="distance", y="recession.velocity")
b,a = np.polyfit(hubble["distance"], hubble["recession.velocity"], deg=1)
x = np.linspace(hubble["distance"].min(), hubble["distance"].max())
plt.plot(x, a+b*x, c="magenta")

plt.show()

hubble.corr()


# --- 2.5

income = pd.read_table(r"./income.dat", sep=" ")
income.head()

inc_2005=income["Income2005"]
afqt=income["AFQT"]

income.plot(kind="scatter", x="AFQT", y="Income2005")
b, a = np.polyfit(afqt, inc_2005, deg=1)
x = np.linspace(afqt.min(), afqt.max())
plt.plot(x, a+b*x, c="orange")
plt.show()

b, a

income.corr() # keine Korrelation zwischen AFQT und Income2005


educ=income["Educ"]

income.plot(kind="scatter", x="Educ", y="Income2005")
b, a = np.polyfit(educ, inc_2005, deg=1)
x = np.linspace(educ.min(), educ.max())
plt.plot(x, a+b*x, c="orange")
plt.show()

b, a

income.corr() # keine Korrelation zwischen AFQT und Educ

x1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]) 
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]) 
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]) 
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])


plt.subplot(221)
x1.plot(kind="scatter")
b, a = np.polyfit(x1, y1, deg=1)
x = np.linspace(x1.min(), x1.max())
plt.plot(x, a+b*x, c="violet")

plt.subplot(222)
b, a = np.polyfit(x1, y1, deg=1)
x = np.linspace(x1.min(), x1.max())
plt.plot(x, a+b*z, c="violet")