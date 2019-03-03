#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:48:30 2019

@author: christopher
"""

import matplotlib.pyplot as plt
import scipy.stats as st
import pandas as pd
import numpy as np
from pandas import Series

# --- 4.2
n=100
m=500

ran = np.array(st.norm.rvs(size=n*m)) 
sim = ran.reshape((n,m))

plt.plot(sim)
plt.show()


plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=1000) 
y = st.norm.pdf(x)

plt.plot(x,y) 
plt.title("Histogramm sim") 
plt.show()

sim_mean = sim.mean(axis=0)

plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=1000)
y = st.norm.pdf(x, loc=0, scale=1/np.sqrt(n))

plt.plot(x,y) 
plt.title("Histogramm sim_mean")
plt.show()


w_95o25 = st.norm.cdf(x=95, loc=100, scale=2)


# --- 4.4
w_X1 = st.norm.cdf(x=2, loc=1, scale=2) - st.norm.cdf(x=0, loc=1, scale=2)
w_Sn = st.norm.cdf(x=51, loc=50, scale=np.sqrt(200)) - st.norm.cdf(x=49, loc=50, scale=np.sqrt(200))
w_Xn = st.norm.cdf(x=2, loc=1, scale=np.sqrt(4/50)) - st.norm.cdf(x=0, loc=1, scale=np.sqrt(4/50))


# 4.5
methodeA = Series([79.98, 80.04, 80.02, 80.04, 80.03, 80.03, 80.04, 79.97, 80.05, 80.03, 80.02, 80.00, 80.02])
methodeB = Series([80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 79.97])

EwA = methodeA.mean()
aSfA = methodeA.std() / np.sqrt(methodeA.size)
rSfA = aSfA / EwA * 100

EwB = methodeB.mean()
aSfB = methodeB.std() / np.sqrt(methodeB.size)
rSfB = aSfB / EwA * 100
