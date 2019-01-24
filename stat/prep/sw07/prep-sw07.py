#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 20:26:56 2019

@author: christopher
"""

# --- 7.1

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt 
from scipy.stats import uniform



x = np.loadtxt(r"oldfaithful.txt").astype(int)
n = np.mean(x)
nboot = 1000.0
tmpdata = np.random.choice(x, n*nboot, replace=True) 
bootstrapsample = np.reshape(tmpdata, (n, nboot)) 
xbarstar = np.mean(bootstrapsample, axis=0)


d = np.percentile(xbarstar, q=[2.5, 97.5])
print('Vertrauensintervall: ',d)

# --- 7.3
q_0d975 = st.norm.ppf(q=0.975, loc=0, scale=1)
progI   = st.norm.interval(alpha=0.95, loc=5, scale=5/np.sqrt(3*60))



n = 60 # Anzahl Stichproben
# X_1,...,X_n simulieren und in einer
# n-spaltigen Matrix (mit 200 Zeilen) anordnen 
sim = uniform.rvs(size=200*n, loc=0, scale=1) 
sim = sim.reshape(200, n)
#In jeder Matrixzeile Mittelwert berechnen

sim_mean = sim.mean(axis=1) 
plt.plot(np.arange(1,201,1),sim_mean)
# Zeichnen Sie mit axhline(y=...) die
# Intervallgrenzen des Prognoseintervalls 
# in der obigen Graphik ein.
plt.axhline(y=5.73, linewidth=4, color='b') 
plt.axhline(y=4.27, linewidth=4, color='b')

n = 60
sim = uniform.rvs(size=200*n, loc=0, scale=10) 
sim = sim.reshape(200, n)
d = np.sum(sim_mean>5.73) + np.sum(sim_mean<4.27) 
print(d)

from scipy.stats import probplot
probplot(sim_mean, plot=plt)


# --- 7.3
interval_99 = st.norm.interval(alpha=0.99, loc=31, scale=6/np.sqrt(10))



# --- 7.4
q_0d95 = st.norm.ppf(q=0.95, loc=0, scale=1/np.sqrt(8))
interval_0d95 = st.norm.interval(alpha=0.95, loc=-403, scale=3.127/np.sqrt(9))

tInterval_0d95 = st.t.interval(alpha=0.95, df=4, loc=512, scale=np.sqrt(106.5)/np.sqrt(5))

zsInterval = st.norm.interval(alpha=0.95, loc=512, scale=np.sqrt(106.5)/np.sqrt(5))