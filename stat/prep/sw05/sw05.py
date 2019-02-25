#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:33:11 2019

@author: christopher
"""

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series, DataFrame


# =============================================================================
# 5.1
# =============================================================================
x = st.norm.rvs(size=1000)
st.probplot(x,plot=plt)



# =============================================================================
# 5.2
# =============================================================================
# moegliche Werte von X
werte = np.array([0,10,11]) # X simulieren
sim = Series(np.random.choice(werte, size=1000, replace=True))
# Mehrere Grafiken neben- und untereinander
plt.subplot(4,2,1)
# Histogramm erstellen
sim.hist(bins=[0,1,10,11,12], edgecolor="black") 
plt.title("Original")
plt.subplot(4,2,2)
# Normalplot erstellen
st.probplot(sim,plot=plt) 
plt.title("Normal Q-Q Plot")


n=200
# X_1,...,X_n simulieren und in einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = np.random.choice(werte, size=n*1000, replace=True) 
sim = DataFrame(np.reshape(sim,(n,1000)))
#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
plt.subplot(4,2,3) 
sim_mean.hist(edgecolor="black") 
plt.title("Mittelwerte von 5 Beobachtungen")
plt.subplot(4,2,4) 
st.probplot(sim_mean,plot=plt) 
plt.title("Normal Q-Q Plot")


X_n = sim.mean().mean()
std_X_n = sim.mean().std()



# =============================================================================
# 5.3
# =============================================================================
iron = pd.read_table("./ironF3.dat",sep=" ",index_col=False)

iron.plot(kind="box")
plt.ylabel("Eisengehalt (Prozent)")
plt.show()

np.log(iron).plot(kind="box")
plt.ylabel("Eisengehalt (Log)")
plt.show()

st.probplot(iron["medium"], plot=plt)
st.probplot(np.log(iron["medium"]), plot=plt)

iron_ew = iron["medium"].mean()
iron_var = iron["medium"].var()

prob_10 = 1 - st.norm.cdf(x=10, loc=iron_ew, scale=np.sqrt(iron_var))

iron_log_ew = np.log(iron["medium"]).mean()
iron_log_var = np.log(iron["medium"]).var()



# =============================================================================
# 5.4
# =============================================================================
f = DataFrame([16.9,4.20,6.70,8.83,10.7,22.4,1.37,3.00,4.82,4.53,6.77,4.81])

st.probplot(f[0], plot=plt)


# =============================================================================
# 5.5
# =============================================================================
u = st.uniform.rvs(size=1000, loc=0, scale=1)

x = DataFrame(-np.log(1 - u) / 2)

x.plot(kind="hist")

st.probplot(x[0], plot=plt)