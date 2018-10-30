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
import math


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


# --- c.) n = 10 und n = 200

n=10

# X_1,...,X_n simulieren und in einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = np.random.choice(werte, size=n*1000, replace=True) 

sim = DataFrame(np.reshape(sim,(n,1000)))

#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
std = sim_mean.std()

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
std = sim_mean.std()

plt.subplot(4,2,3) 

sim_mean.hist(edgecolor="black") 
plt.title("Mittelwerte von 5 Beobachtungen")

plt.subplot(4,2,4) 
probplot(sim_mean,plot=plt) 
plt.title("Normal Q-Q Plot")

# Immer stärker Normalverteilt


##################################################

# AUFGABE 5.3

##################################################


iron = pd.read_table("ironF3.dat",sep=" ",index_col=False)


# --- a.) Boxplot
# Sie unterscheiden sich in ihrer Streuung und Wertebereich
# High: am meisten normalverteilt im Vergleich zu den anderen mit einem Ausreisser nach oben
# Medium: eher linksschief mit "Ausreisser" um 15
# Low: Schwierig zu sagen, was für eine Verteilung
iron.plot(kind="box")

# --- b.) Boxplot logarithmieren mit log(iron)
# Die Streuung hat sich ausgeglichen...

np.log(iron).plot(kind="box",ax=plt.gca()) 
plt.ylabel("log(iron)")


# --- c.) Check Normalverteilung
# Logarithmische Verteilung scheint besser zu passen...
probplot(iron["high"], plot=plt)
probplot(iron["medium"], plot=plt)
probplot(iron["low"], plot=plt)

probplot(np.log(iron["high"]), plot=plt)
probplot(np.log(iron["medium"]), plot=plt)
probplot(np.log(iron["low"]), plot=plt)

# --- d.) Parameter und Wahrscheinlichkeit
# Erwartungswert
iron.mean()
# Varianz
iron.var()

# Wahrscheinlichkeit
w_10 = 1 - norm.cdf(x=10, loc=iron.mean(), scale=np.sqrt(iron.var()))

# High: 0.009589
# Medium: 0.370805
# Low: 0.598319

# --- e.) Log-Verteilung
# Erwartungswert (log)
loc = np.log(iron["medium"]).mean()

# Varianz (log)
var = np.log(iron["medium"]).var()

# Wahrscheinlichkeit (log)
w_10_log = 1 - norm.cdf(x=np.log(10), loc=loc, scale=np.sqrt(var))
# 0.27097597476867175


##################################################

# AUFGABE 5.4

##################################################


# --- a.) Momentenmethode
# Erwartungswert
e = 120 / 15 # 8 => Erwartungswert (lambda) = 1/8

# Exponentialverteilt
P = 1 - (1 - math.exp(-12/8)) = 0.22313

# Erwartungswert für 12min
e12 = 15 / 120 * 12 # 1.5

# Wahrscheinlichkeit innerhalb 12min 2 Fische
P2F = math.exp(-12/8) * ((1.5**2)/math.factorial(2)) # 0.25102
