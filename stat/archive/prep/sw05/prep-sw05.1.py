#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:40:53 2019

@author: christopher
"""

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series, DataFrame


# --- 5.1

plt.subplot(221)
x = st.norm.rvs(size=10)
st.probplot(x,plot=plt)
plt.title("10 Zufallszahlen")

plt.subplot(222)
x = st.norm.rvs(size=20)
st.probplot(x,plot=plt)
plt.title("20 Zufallszahlen")

plt.subplot(223)
x = st.norm.rvs(size=100)
st.probplot(x,plot=plt)
plt.title("100 Zufallszahlen")

plt.tight_layout()
plt.show()


plt.subplot(221)
x = st.t.rvs(size=10, df=20)
st.probplot(x,plot=plt)
plt.title("10 Zufallszahlen, 20 FG")

plt.subplot(222)
x = st.t.rvs(size=20, df=20)
st.probplot(x,plot=plt)
plt.title("20 Zufallszahlen, 20 FG")

plt.subplot(223)
x = st.t.rvs(size=100, df=20)
st.probplot(x,plot=plt)
plt.title("100 Zufallszahlen, 20 FG")

plt.tight_layout()
plt.show()



plt.subplot(221)
x = st.t.rvs(size=10, df=7)
st.probplot(x,plot=plt)
plt.title("10 Zufallszahlen, 7 FG")

plt.subplot(222)
x = st.t.rvs(size=20, df=7)
st.probplot(x,plot=plt)
plt.title("20 Zufallszahlen, 7 FG")

plt.subplot(223)
x = st.t.rvs(size=100, df=7)
st.probplot(x,plot=plt)
plt.title("100 Zufallszahlen, 7 FG")

plt.tight_layout()
plt.show()



plt.subplot(221)
x = st.t.rvs(size=10, df=3)
st.probplot(x,plot=plt)
plt.title("10 Zufallszahlen, 3 FG")

plt.subplot(222)
x = st.t.rvs(size=20, df=3)
st.probplot(x,plot=plt)
plt.title("20 Zufallszahlen, 3 FG")

plt.subplot(223)
x = st.t.rvs(size=100, df=3)
st.probplot(x,plot=plt)
plt.title("100 Zufallszahlen, 3 FG")

plt.tight_layout()
plt.show()


# --- 5.2

# moegliche Werte von X
werte = np.array([0,10,11]) 

# X simulieren
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
st.probplot(sim_mean,plot=plt) 
plt.title("Normal Q-Q Plot")

plt.tight_layout()
plt.show()



n=10
# X_1,...,X_n simulieren und in einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = np.random.choice(werte, size=n*1000, replace=True) 

sim = DataFrame(np.reshape(sim,(n,1000)))
#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
plt.subplot(4,2,3) 

sim_mean.hist(edgecolor="black") 

plt.title("Mittelwerte von 10 Beobachtungen")

plt.subplot(4,2,4) 
st.probplot(sim_mean,plot=plt) 
plt.title("Normal Q-Q Plot")

plt.tight_layout()
plt.show()



n=200
# X_1,...,X_n simulieren und in einer n-spaltigen
# Matrix (mit 1000 Zeilen) anordnen
sim = np.random.choice(werte, size=n*1000, replace=True) 

sim = DataFrame(np.reshape(sim,(n,1000)))
#In jeder Matrixzeile Mittelwert berechnen
sim_mean = sim.mean()
plt.subplot(4,2,3) 

sim_mean.hist(edgecolor="black") 

plt.title("Mittelwerte von 200 Beobachtungen")

plt.subplot(4,2,4) 
st.probplot(sim_mean,plot=plt) 
plt.title("Normal Q-Q Plot")

plt.tight_layout()
plt.show()


# sim_mean.mean()
sim_var = 1/200**2 * ((0 - 7)**2 + (10 - 7)**2 + (11 - 7)**2)


# --- 5.3
iron = pd.read_table("ironF3.dat",sep=" ",index_col=False)

iron.plot(kind="box")

iron_log = np.log(iron)
iron_log.plot(kind="box")

plt.subplot(221)
st.probplot(iron["medium"], plot=plt)
plt.title("Medium Dosis")

plt.subplot(222)
st.probplot(iron_log["medium"], plot=plt)
plt.title("Medium Dosis (Log)")
plt.show()


iron_mean = iron["medium"].mean()
iron_var = iron["medium"].var()
iron_std = iron["medium"].std()

# 0.37080583780045573
1 - st.norm.cdf(x=10, loc=iron_mean, scale=iron_std)


iron_log_mean = iron_log["medium"].mean()
iron_log_var = iron_log["medium"].var()
iron_log_std = iron_log["medium"].std()

# 0.2710978359464026
1 - st.norm.cdf(x=np.log(10), loc=iron_log_mean, scale=iron_log_std)



fische = Series([16.9, 4.20, 6.70, 8.83, 10.7, 22.4, 1.37, 3.00, 4.82, 4.53, 6.77, 4.81])
st.probplot(fische, plot=plt)


# --- 5.5
unif = Series(st.uniform.rvs(size=1000, loc=0, scale=1))
x = -np.log(unif) / 2
x.plot(kind="hist")
plt.show()


expon = Series(st.expon.rvs(size=1000, scale=1/2))
x.plot(kind="hist")
plt.show()

st.probplot(x, plot=plt)