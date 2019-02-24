#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 16:08:41 2019

@author: christopher
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# =============================================================================
# 2.2
# =============================================================================
d1 = pd.read_csv("./klaerschlamm.dat", sep=" ", index_col=0)
d1.drop("Labor", 1)
d1.head()
d1.mean()["Pr1"]

d1.plot(kind="box")
# 1, 4, 9 (4, 6)


# =============================================================================
# 2.3
# =============================================================================

hubble = pd.read_table("./hubble.txt", sep=" ")

hubble.plot(kind="scatter", x="distance", y="recession.velocity")
beta0, beta1 = np.polyfit(x=hubble["distance"], y=hubble["recession.velocity"], deg=1)

x = np.linspace(hubble["distance"].min(), hubble["distance"].max())

plt.plot(x, beta0+beta1*x)
plt.show()

hubble.corr()