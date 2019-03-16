#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 08:02:53 2019

@author: christopher
"""
# =============================================================================
# Imports
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
from scipy.stats import norm, binom, uniform


# =============================================================================
# Examples
# =============================================================================
norm.cdf(x=5100, loc=5000, scale=np.sqrt(2500))
binom.cdf(k=5100, n=10000, p=0.5)

1 - norm.cdf(x=0, loc=270.27, scale=99.96)


# =============================================================================
# 4.2
# =============================================================================

# Random seed sorgt dafür, dass immer 
# dieselben Zufallszahlen generiert werden
np.random.seed(13)

# 500 Stichproben aus einer
# Standardnormalverteilung mit Umfang n=5
u = 5
m = 500
sp = np.array(norm.rvs(size=u*m))

# Array aufteilen in die 5 Durchführungen
sim = sp.reshape((u, m))

plt.plot(sim)
plt.show()

plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100) 
y = norm.pdf(x)
plt.plot(x, y)
plt.show()


sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(u))
plt.plot(x,y) 
plt.title("Histogramm sim_mean")
plt.show()


u = 2
m = 500
sp = np.array(norm.rvs(size=u*m))

# Array aufteilen in die 5 Durchführungen
sim = sp.reshape((u, m))

plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100) 
y = norm.pdf(x)
plt.plot(x, y)
plt.show()


sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(u))
plt.plot(x,y) 
plt.title("Histogramm sim_mean")
plt.show()


u = 10
m = 500
sp = np.array(norm.rvs(size=u*m))

# Array aufteilen in die 5 Durchführungen
sim = sp.reshape((u, m))

plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100) 
y = norm.pdf(x)
plt.plot(x, y)
plt.show()


sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(u))
plt.plot(x,y) 
plt.title("Histogramm sim_mean")
plt.show()


u = 100
m = 500
sp = np.array(norm.rvs(size=u*m))

# Array aufteilen in die 5 Durchführungen
sim = sp.reshape((u, m))

plt.hist(sim.T, bins=20, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100) 
y = norm.pdf(x)
plt.plot(x, y)
plt.show()


sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black", facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(u))
plt.plot(x,y) 
plt.title("Histogramm sim_mean")
plt.show()



# =============================================================================
# 4.3
# =============================================================================

# E(X) = 100
# std = 10
# n = 25
p1 = norm.cdf(95, loc=100, scale=10/np.sqrt(25))
p2 = uniform.cdf()


# =============================================================================
# 4.4
# =============================================================================

p3 = norm.cdf(2, loc=1, scale=2)
p4 = norm.cdf(x=[49, 51], loc=50, scale=np.sqrt(200))
p4 = p4[1] - p4[0]
p5 = norm.cdf(2, loc=1, scale=np.sqrt(2)/5)


# =============================================================================
# 4.5
# =============================================================================
methode_A = Series([79.98, 80.04, 80.02, 
                    80.04, 80.03, 80.03, 
                    80.04, 79.97, 80.05, 
                    80.03, 80.02, 80.00, 
                    80.02])

methode_B = Series([80.02, 79.94, 79.98, 
                    79.97, 79.97, 80.03, 
                    79.95, 79.97])

mean_A = methode_A.mean()
mean_B = methode_B.mean()

stf_A = methode_A.std() / np.sqrt(methode_A.size)
stf_B = methode_B.std() / np.sqrt(methode_B.size)

rel_A = stf_A / mean_A * 100
rel_B = stf_B / mean_B * 100
