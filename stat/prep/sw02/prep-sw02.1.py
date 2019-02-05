#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:41:50 2019

@author: christopher
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

schlamm = pd.read_table(r"klaerschlamm.dat", sep=" ", index_col=0)

schlamm = schlamm.drop("Labor",1) 
schlamm.head()

schlamm.describe()
schlamm.plot(kind="box")

(schlamm.median()-schlamm.mean()).std()

(schlamm.median()-schlamm.mean())


schlamm_centered = schlamm - schlamm.median()
schlamm_centered.T.plot(kind="box")
plt.tight_layout()
plt.show()


hubble = pd.read_table("hubble.txt", sep=" ")
hubble
hubble.plot(kind="scatter", x="distance", y="recession.velocity")
b, a = np.polyfit(hubble["distance"], hubble["recession.velocity"], deg=1)
x = np.linspace(hubble["distance"].min(), hubble["distance"].max())
plt.plot(x, a+b*x, c="orange")
plt.show()

hubble.corr()



income = pd.read_table(r"income.dat", sep=" ")
income.head()

income.plot(kind="scatter", x="Income2005", y="Educ")
income.plot(kind="scatter", x="Income2005", y="AFQT")


b1, a1 = np.polyfit(income["Income2005"])