#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:11:47 2019

@author: christopher
"""

import scipy.stats as st
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import numpy as np
import pandas as pd


# --- 5.1
z_10 = st.norm.rvs(size=10)
z_20 = st.norm.rvs(size=20)
z_50 = st.norm.rvs(size=50)
z_100 = st.norm.rvs(size=100)

st.probplot(z_10, plot=plt)
st.probplot(z_20, plot=plt)
st.probplot(z_50, plot=plt)
st.probplot(z_100, plot=plt)


x = st.t.rvs(size=20, df=20)
st.probplot(x, plot=plt)

x = st.t.rvs(size=20, df=7)
st.probplot(x, plot=plt)

x = st.t.rvs(size=20, df=3)
st.probplot(x, plot=plt)


x = st.t.rvs(size=100, df=20)
st.probplot(x, plot=plt)

x = st.t.rvs(size=100, df=7)
st.probplot(x, plot=plt)

x = st.t.rvs(size=100, df=3)
st.probplot(x, plot=plt)


plt.subplot(221)
x = st.chi2.rvs(size=20, df=20)
st.probplot(x, plot=plt)

plt.subplot(222)
x = st.chi2.rvs(size=100, df=20)
st.probplot(x, plot=plt)

plt.subplot(223)
x = st.chi2.rvs(size=20, df=1)
st.probplot(x, plot=plt)

plt.subplot(224)
x = st.chi2.rvs(size=100, df=1)
st.probplot(x, plot=plt)

plt.tight_layout()
plt.show()



# --- 5.2

# moegliche Werte von X
werte = np.array([0,10,11])

# X simulieren
sim = Series(np.random.choice(werte, size=1000, replace=True))

# Mehrere Grafiken neben- und untereinander
plt.subplot(221)

# Histogramm erstellen
sim.hist(bins=[0,1,10,11,12], edgecolor="black") 
plt.title("Original")


plt.subplot(222)


# Normalplot erstellen
st.probplot(sim,plot=plt) 
plt.title("Normal Q-Q Plot")
plt.show()



n = 5

# X_1,...,X_n simulieren und in einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = np.random.choice(werte, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim,(n,1000)))


std_n5 = sim.std() / sim.size


#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
plt.subplot(4,2,3)
sim_mean.hist(edgecolor="black")
plt.title("Mittelwerte von 5 Beobachtungen")


plt.subplot(4,2,4)
st.probplot(sim_mean,plot=plt)
plt.title("Normal Q-Q Plot")



n = 10

# X_1,...,X_n simulieren und in einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = np.random.choice(werte, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim,(n,1000)))


#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
plt.subplot(4,2,5)
sim_mean.hist(edgecolor="black")
plt.title("Mittelwerte von 10 Beobachtungen")


plt.subplot(4,2,6)
st.probplot(sim_mean,plot=plt)
plt.title("Normal Q-Q Plot")


Standardfehler_X10 = sim_mean.std()


n = 200

# X_1,...,X_n simulieren und in einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = np.random.choice(werte, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim,(n,1000)))


#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
plt.subplot(4,2,7)
sim_mean.hist(edgecolor="black")
plt.title("Mittelwerte von 200 Beobachtungen")


plt.subplot(4,2,8)
st.probplot(sim_mean,plot=plt)
plt.title("Normal Q-Q Plot")

plt.tight_layout()
plt.show()


Erwartungswert_Xn = 1/3 * (0 + 10 + 11)
Standardfehler_X200 = sim_mean.std()


# --- 5.3

iron = pd.read_table(r"ironF3.dat", sep=" ", index_col=False)
iron.describe()
iron.median()

iron.plot(kind="box", title="Eisen")

# Je mehr Eisen gegeben, desto weniger wird absorbiert
# Je mehr Eisen, desto grösser die Streuung

iron_log = np.log(iron)
iron_log.plot(kind="box", title="Logarithmierte Eisenwerte")

# Varianz wird "stabilisiert"

plt.subplot(221)
st.probplot(iron["medium"], plot=plt)
plt.title("Normalplot: Medium Dose")

plt.subplot(222)
st.probplot(iron_log["medium"], plot=plt)
plt.title("Normalplot: Medium Dose (log)")

plt.tight_layout()
plt.show()


iron_mean = iron["medium"].mean()
iron_var = iron["medium"].var()
iron_10 = 1 - st.norm.cdf(x=10, loc=iron_mean, scale=np.sqrt(iron_var))



iron_log_mean = iron_log["medium"].mean()
iron_log_var = iron_log["medium"].var()
iron_log_10 = 1 - st.norm.cdf(x=np.log(10), loc=iron_log_mean, scale=np.sqrt(iron_log_var))




# --- 5.4

fische = Series([16.9, 4.20, 6.70, 8.83, 10.7, 22.4, 1.37, 3.00, 4.82, 4.53, 6.77, 4.81])

st.probplot(fische, plot=plt)



# --- 5.5

x = Series(st.uniform.rvs(size=1000, loc=0, scale=1))
arrivals = np.log(x) / -2
sim_exp = Series(st.expon.rvs (size=1000))

plt.subplot(221)
arrivals.plot(kind="hist", edgecolor="blue")
plt.title("uniform")

plt.subplot(222)
sim_exp.plot(kind="hist", edgecolor="green")
plt.title("expon")

plt.subplot(223)
st.probplot(arrivals, plot=plt)

plt.subplot(224)
st.probplot(sim_exp, plot=plt)

plt.tight_layout()
plt.show()



# --- 5.6

5/(np.log(12.0)+np.log(4.0)+np.log(6.9)+np.log(27.9)+np.log(15.4))

x = np.array([12.0,4.0,6.9,27.9,15.4]) 
np.mean(x)/(np.mean(x)-1)
