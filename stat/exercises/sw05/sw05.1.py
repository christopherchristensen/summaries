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


# 10 Durchführungen von X
n = 10

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


# 200 Durchführungen von X
n = 200

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

print(sim_mean.mean())
print(sim_mean.std())


# =============================================================================
# 5.3
# =============================================================================
iron = DataFrame(pd.read_table("ironF3.dat", sep=" ", index_col=False))

# a.)

# Sie unterscheiden sich in der Lage und
# in der Streuung.

# High: Kleine Streuung, Lage bei unter 5 
#       (wenig Eisen zurückgeblieben)
# Medium: Mittlere Streuung, Linksseitige Verteilung
# Low: Grösste Streuung, Linksseitige Verteilung,
#      höherer Anteil Eisen zurückgeblieben
iron.plot(kind="box")

#b.)

# Streuung wurde stabilisiert
np.log(iron).plot(kind="box")

# c.)

plt.subplot(221)
st.probplot(iron['high'], plot=plt)

plt.subplot(222)
st.probplot(iron['medium'], plot=plt)

plt.subplot(223)
st.probplot(iron['low'], plot=plt)
plt.show()


# Stärker normalverteilt
plt.subplot(221)
st.probplot(np.log(iron['high']), plot=plt)

plt.subplot(222)
st.probplot(np.log(iron['medium']), plot=plt)

plt.subplot(223)
st.probplot(np.log(iron['low']), plot=plt)

plt.show()


# d.)
iron_mu  = iron['medium'].mean()
iron_var = iron['medium'].var()

# 1 - 62.92 %
iron_p10 = st.norm.cdf(10, loc=iron_mu, scale=np.sqrt(iron_var))

# e.)

#  1 - 72.89 % 
iron_log_p10 = st.norm.cdf(np.log(10), loc=np.log(iron['medium']).mean(), scale=np.log(iron['medium']).std())


# =============================================================================
# 5.4
# =============================================================================
f1 = DataFrame([16.9, 4.20, 6.70, 8.83, 10.7, 22.4, 1.37, 3.00, 4.82, 4.53, 6.77, 4.81])

# [((f1.index + 1) - 0.5)/f1.size] ist das alpha_k
# Danach wird es angepasst an die Verteilung mit -np.log(1-alpha_k)
f2 = DataFrame({
    "Theoretical Quantiles": -np.log(1 - (((f1.index + 1) - 0.5)/f1.size)),
    "Ordered Values": f1.sort_values(by=0).loc[:,0].reset_index(drop=True)
})
f2.describe()
f2.plot(kind="scatter", x="Theoretical Quantiles", y="Ordered Values")

b, a = np.polyfit(f2["Theoretical Quantiles"], f2["Ordered Values"], deg=1)
x = np.linspace(f2["Theoretical Quantiles"].min(), f2["Theoretical Quantiles"].max())

plt.plot(x, a + b * x, c='orange')

plt.show()


# =============================================================================
# 5.5
# =============================================================================
n = 1000

unif = st.uniform.rvs(size=n, loc=0, scale=1)
x = Series(-np.log(1-unif) / 2)
x_expon = Series(st.expon.rvs(size=n, loc=2))

plt.subplot(121)
x.hist(bins=30)

plt.subplot(122)
x_expon.hist(bins=30)

plt.show()

alpha_k = (x.index - 0.5) / x.size
x_quantile = -np.log(1 - alpha_k) / 2

qq = DataFrame({
    "Ordered Values": x.sort_values(axis=0).reset_index(drop=True),
    "Theoretical Quantiles": x_quantile
})

qq.plot(kind="scatter", x="Theoretical Quantiles", y="Ordered Values")

b, a = np.polyfit(x=qq["Theoretical Quantiles"], y=qq["Ordered Values"], deg=1)
x = np.linspace(qq["Theoretical Quantiles"].min(), qq["Theoretical Quantiles"].max())

plt.plot(x, a + b * x, c='orange')

plt.show()