#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:10:51 2019

@author: christopher
"""

# =============================================================================
# Imports
# =============================================================================
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

from pandas import Series, DataFrame

# =============================================================================
# 5.1
# =============================================================================

np.random.seed(13)
# Normalverteilte Zufallszahlen
# n = 10
plt.subplot(221)
x = st.norm.rvs(size=10)
st.probplot(x, plot=plt)

# n = 20
plt.subplot(222)
x = st.norm.rvs(size=20)
st.probplot(x, plot=plt)

# n = 50
plt.subplot(223)
x = st.norm.rvs(size=50)
st.probplot(x, plot=plt)

# n = 100
plt.subplot(224)
x = st.norm.rvs(size=100)
st.probplot(x, plot=plt)

plt.tight_layout()
plt.show()

# T-verteilte Zufallszahlen
# mit 3 Freiheitsgraden

# Mit dieser Übung wird überprüft
# wie stark sich die Normalverteilung
# von der t-Verteilung unterscheidet

# n = 10
plt.subplot(221)
x = st.t.rvs(size=10, df=3)
st.probplot(x, plot=plt)

# n = 20
plt.subplot(222)
x = st.t.rvs(size=20, df=3)
st.probplot(x, plot=plt)

# n = 50
plt.subplot(223)
x = st.t.rvs(size=50, df=3)
st.probplot(x, plot=plt)

# n = 100
plt.subplot(224)
x = st.t.rvs(size=100, df=3)
st.probplot(x, plot=plt)

plt.tight_layout()
plt.show()


# T-verteilte Zufallszahlen
# mit 7 Freiheitsgraden

# n = 10
plt.subplot(221)
x = st.t.rvs(size=10, df=7)
st.probplot(x, plot=plt)

# n = 20
plt.subplot(222)
x = st.t.rvs(size=20, df=7)
st.probplot(x, plot=plt)

# n = 50
plt.subplot(223)
x = st.t.rvs(size=50, df=7)
st.probplot(x, plot=plt)

# n = 100
plt.subplot(224)
x = st.t.rvs(size=100, df=7)
st.probplot(x, plot=plt)

plt.tight_layout()
plt.show()



# T-verteilte Zufallszahlen
# mit 20 Freiheitsgraden

# n = 10
plt.subplot(221)
x = st.t.rvs(size=10, df=20)
st.probplot(x, plot=plt)

# n = 20
plt.subplot(222)
x = st.t.rvs(size=20, df=20)
st.probplot(x, plot=plt)

# n = 50
plt.subplot(223)
x = st.t.rvs(size=50, df=20)
st.probplot(x, plot=plt)

# n = 100
plt.subplot(224)
x = st.t.rvs(size=100, df=20)
st.probplot(x, plot=plt)

plt.tight_layout()
plt.show()



# Chi-verteilte Zufallszahlen
# mit 1 Freiheitsgrad

# n = 20
plt.subplot(221)
x = st.t.rvs(size=20, df=1)
st.probplot(x, plot=plt)

# n = 100
plt.subplot(222)
x = st.t.rvs(size=100, df=1)
st.probplot(x, plot=plt)

plt.tight_layout()
plt.show()



# Chi-verteilte Zufallszahlen
# mit 20 Freiheitsgrad

# n = 20
plt.subplot(222)
x = st.t.rvs(size=20, df=20)
st.probplot(x, plot=plt)


# n = 100
plt.subplot(224)
x = st.t.rvs(size=100, df=20)
st.probplot(x, plot=plt)

plt.tight_layout()
plt.show()


# =============================================================================
# 5.2
# =============================================================================

# Mögliche Werte
werte = np.array([0,10,11])

# Zufallszahlen (X) simulieren
sim = Series(np.random.choice(werte, size=1000, replace=True))


# Histogramm der simulierten Zufallszahlen
# Diese sind offensichtlich uniform verteilt,
# denn jede Zahl wird mit einer Wahrscheinlichkeit
# 1/3 erstellt
plt.subplot(4,2,1)
sim.hist(bins=[0,1,10,11,12], edgecolor="black") 
plt.title("Original")

# Normalplot der simulierten Zufallszahlen
# Diese sind offensichtlich nicht normalverteilt
plt.subplot(4,2,2)
st.probplot(sim,plot=plt) 
plt.title("Normal Q-Q Plot")

plt.show()



# 5 Durchführungen von X
n = 5

# X_1,...,X_n simulieren
sim = np.random.choice(werte, size=n*1000, replace=True) 

# In einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = DataFrame(np.reshape(sim,(n,1000)))

#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
plt.subplot(4,2,3) 
sim_mean.hist(edgecolor="black") 
plt.title("Mittelwerte von 5 Beobachtungen")

plt.subplot(4,2,4) 
st.probplot(sim_mean,plot=plt) 
plt.title("Normal Q-Q Plot")

plt.show()


# =============================================================================
# 5.3
# =============================================================================

