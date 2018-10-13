#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:20:41 2018

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

# AUFGABE 3.4

##################################################


# --- b.) Kummulative Verteilungsfunktion I
# CDF erstellt eine kummulative Verteilungsfunktion 
# mit den gegebenen Werten. 
# Immer wenn man den "höchstens"-Wert einer normalen
# Verteilung berechnen müssen, verwendet man norm.cdf.
# x = "höchstens", loc = Erwartungswert
P1 = norm.cdf(x=40, loc=32, scale=6); # 0.9087887802741321

# --- Standardisierte Zufallsvariable Z
# x = (Höchstens - Erwartungswert) / Standardabweichung
P2 = norm.cdf(x=(40 - 32)/6); # 0.9087887802741321

# --- c.) Kummulative Verteilungsfunktion II
P3 = norm.cdf(x=27, loc=32, scale=6); # 0.20232838096364308

# --- d.) Wahrscheinlichkeitsdichtefunktion I
# Wir suchen die Zufallsvariable, die mit 97.5% 
# Wahrscheinlichkeit unterschritten wird.
P4 = norm.ppf(q=0.975, loc=32, scale=6); # 43.759783907240326

# --- e.) Wahrscheinlichkeitsdichtefunktion II
# Gleiches Verfahren wie in Teilaufgabe d.)
P5 = norm.ppf(q=0.1, loc=32, scale=6); # 24.310690606732397

# --- f.) Wahrscheinlichkeit eines Intervals
P6 = norm.cdf(x=32+6, loc=32, scale=6) # 0.8413447460685429
P7 = norm.cdf(x=32-6, loc=32, scale=6) # 0.15865525393145707
P8 = P6 - P7 # 0.6826894921370859


##################################################

# AUFGABE 3.5

##################################################


# --- a.) kummulative Verteilungsfunktion
# Wir berechnen nun das Gegenteil von "höchsten" 
# eine Zufallsvariable. Also: 1 - "höchsten" 
# Zufallsvariable X
P9 = 1 - norm.cdf(x=0.9, loc=0, scale=0.45); # 0.02275013194817921

# --- b.) Quantile
P10 = norm.ppf(q=0.005, loc=0, scale=0.45); # -1.1591231865970053

# --- c.) kummulative Verteilungsfunktion
P11 = norm.cdf(x=0.9, loc=1.8, scale=0.45); # 0.022750131948179195


##################################################

# AUFGABE 3.6

##################################################


# --- a.) kummulative Verteilungsfunktion
P12 = norm.cdf(x=0.2515, loc=0.2508, scale=0.0005) - norm.cdf(x=0.2485, loc=0.2508, scale=0.0005); # 0.91924122831152
 
# --- b.) kummulative Verteilungsfunktion
P13 = norm.cdf(x=0.2515, loc=0.2500, scale=0.0005) - norm.cdf(x=0.2485, loc=0.2500, scale=0.0005); # 0.9973002039367398


##################################################

# AUFGABE 3.7

##################################################


x = uniform.rvs(size=10000000, loc=-1, scale=2)
y = uniform.rvs(size=10000000, loc=-1, scale=2)

p_amount_in_circle = np.sum(np.sqrt(x * x + y * y) < 1)