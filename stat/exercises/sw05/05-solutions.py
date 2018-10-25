#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:32:59 2018

@author: christopher
"""

##################################################

# IMPORTS

##################################################

from pandas import Series, DataFrame 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import norm, uniform, probplot, t, chi2
import numpy as np


##################################################

# AUFGABE 5.1

##################################################


# --- a.) Normalverteilte Zufallszahlen

# normalverteilte Zufallszahlen generieren
ran_10 = norm.rvs(size=10) 
ran_20 = norm.rvs(size=20) 
ran_50 = norm.rvs(size=50) 
ran_100 = norm.rvs(size=100)
ran_200 = norm.rvs(size=200)  

# Zufallszahlen plotten (simulieren)
probplot(ran_10, plot=plt)
probplot(ran_20, plot=plt)
probplot(ran_50, plot=plt)
probplot(ran_100, plot=plt)
probplot(ran_200, plot=plt)

# Sie verteilen sich alle entlang derselben Linie?


# --- b.) T-verteilte Zufallszahlen
t_20_20 = t.rvs(size=20, df=20)
t_20_07 = t.rvs(size=20, df=7)
t_20_03 = t.rvs(size=20, df=3)
t_100_20 = t.rvs(size=100, df=20)
t_100_07 = t.rvs(size=100, df=7)
t_100_03 = t.rvs(size=100, df=3)

probplot(t_20_20, plot=plt)
probplot(t_20_07, plot=plt)
probplot(t_20_03, plot=plt)
probplot(t_100_20, plot=plt)
probplot(t_100_07, plot=plt)
probplot(t_100_03, plot=plt)

# Je mehr Zufallszahlen, desto stärker verteilen sie sich entlang derselben Linie?
# Schräger als normalverteilte Zufallszahlen?


# --- c.) Chi-verteilte Zufallszahlen

c_20_20 = chi2.rvs(size=20, df=20)
c_20_01 = chi2.rvs(size=20, df=1)
c_100_20 = chi2.rvs(size=100, df=20)
c_100_01 = chi2.rvs(size=100, df=1)

probplot(c_20_20, plot=plt)
probplot(c_20_01, plot=plt)
probplot(c_100_20, plot=plt)
probplot(c_100_01, plot=plt)

# Sehr stark beinflusst vom Freiheitsgrad!
# Man könnte es auch noch schöner Plotten mit Subplots


##################################################

# AUFGABE 5.2

##################################################


# --- a.) Verteilung von X
# (Vorgegebene) mögliche Werte von X in Array
werte = np.array([0, 10, 11])

# X simulieren
sim = Series(np.random.choice(werte, size=1000, replace=True))

# Mehrere Grafiken neben- und untereinander
plt.subplot(4, 2, 1)

# Histogramm erstellen
sim.hist(bins=[0, 1, 10, 11, 12], edgecolor="black") 
plt.title("Original")

plt.subplot(4, 2, 2)

# Normalplot erstellen
probplot(sim,plot=plt) 
plt.title("Normal Q-Q Plot")


# --- b.) Verteilung vom Mittelwert von mehreren X

n=5

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
probplot(sim_mean,plot=plt) 
plt.title("Normal Q-Q Plot")


n=10

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
probplot(sim_mean,plot=plt) 
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
probplot(sim_mean,plot=plt) 
plt.title("Normal Q-Q Plot")

# Immer stärker Normalverteilt

