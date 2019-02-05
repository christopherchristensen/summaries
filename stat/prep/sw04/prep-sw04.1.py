#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:51:20 2019

@author: christopher
"""

import matplotlib.pyplot as plt 
from scipy.stats import norm 
import numpy as np
from pandas import Series

# --- 4.2

n=5
m = 500
ran = np.array(norm.rvs(size=n*m)) 
sim = ran.reshape((n,m))

plt.plot(sim)
plt.show()


plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100) 
y = norm.pdf(x)
plt.plot(x,y) 
plt.title("Histogramm sim") 
plt.show()



sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")

x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))

plt.plot(x,y) 
plt.title("Histogramm sim_mean")
plt.show()


# --- 4.3

norm.cdf(x=95, loc=100, scale=10/np.sqrt(25)) # 0.0062


# --- 4.4

# 0.3829
norm.cdf(x=2, loc=1, scale=2/np.sqrt(1)) - norm.cdf(x=0, loc=1, scale=2/np.sqrt(1))

# 0.0564
norm.cdf(x=51, loc=50, scale=np.sqrt(200)) - norm.cdf(x=49, loc=50, scale=np.sqrt(200))

# 0.9996
norm.cdf(x=2, loc=1, scale=np.sqrt(0.08)) - norm.cdf(x=0, loc=1, scale=np.sqrt(0.08))


# --- 4.5
methodeA = Series([79.98, 80.04, 80.02, 80.04, 80.03, 80.03, 80.04, 79.97, 80.05, 80.03, 80.02, 80.00, 80.02])
methodeB = Series([80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 79.97])

mA = methodeA.mean()
mB = methodeB.mean()

sA = methodeA.std() / np.sqrt(methodeA.size)
sB = methodeB.std() / np.sqrt(methodeB.size)
