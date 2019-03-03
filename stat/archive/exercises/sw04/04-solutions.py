#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:03:28 2018

@author: christopher
"""


##################################################

# IMPORTS

##################################################

from pandas import Series, DataFrame 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import norm, uniform
import numpy as np


##################################################

# AUFGABE 4.2

##################################################

# Code aus der Aufgabenstellung übernehmen
n = 5
m = 500

# Zufallszahlen generieren (normalverteilt?)
ran = np.array(norm.rvs(size = n * m)) 

# Matrix aus Zufallszahlen erstellen
sim = ran.reshape((n, m))

# --- a.) Stichproben als Runs darstellen
plt.plot(sim)
plt.show()

# --- b.) Mittelwert berechnen und Histogramm
plt.hist(
        sim.T, bins=20, density=True, 
    	edgecolor="black", facecolor="white"
)
                               
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

# --- c.) Wiederholen mit anderen Werten für n

n=2
m = 500

plt.hist(
        sim.T, bins=20, density=True, 
    	edgecolor="black", facecolor="white"
)
                               
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


n=10
m = 500

plt.hist(
        sim.T, bins=20, density=True, 
    	edgecolor="black", facecolor="white"
)
                               
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



n=100
m = 500

plt.hist(
        sim.T, bins=20, density=True, 
    	edgecolor="black", facecolor="white"
)
                               
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


##################################################

# AUFGABE 4.3

##################################################


# --- a.) kummulative Verteilungsfunktion
P1 = norm.cdf(x=95, loc=100, scale=2) # 0.006209665325776132


##################################################

# AUFGABE 4.4

##################################################


# --- a.) kummulative Verteilungsfunktion
P2 = norm.cdf(x=2, loc=1, scale=2) - norm.cdf(x=0, loc=1, scale=2) # 0.38292492254802624
P3 = norm.cdf(x=51, loc=50, scale=14.1421356237) - norm.cdf(x=49, loc=50, scale=14.1421356237) # 0.056371977797139816
P4 = norm.cdf(x=2, loc=1, scale=0.2828) - norm.cdf(x=0, loc=1, scale=0.2828) # 0.9995938696952003



##################################################

# AUFGABE 4.5

##################################################


methodeA = Series([79.98 , 80.04 , 80.02 , 80.04 , 80.03 , 80.03 , 80.04 , 79.97 , 80.05 , 80.03, 80.02 , 80.00 , 80.02])
methodeB = Series([80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 79.97])

meanA = methodeA.mean() # 80.02076923076923
meanB = methodeB.mean() # 79.97875

stdFehlerA = methodeA.std() / np.sqrt(methodeA.size) # 0.00664691353682878
stdFehlerB = methodeB.std() / np.sqrt(methodeB.size) # 0.011090133968017208