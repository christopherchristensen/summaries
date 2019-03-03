#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:39:35 2018

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

# AUFGABE 6.1

##################################################


wf = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])



# 1. Model, Varianz = (1.5)^2
# 2. Nullhypothese H_0: mü = mü_0 = 70 (arithmetische Mittel)
#    Alternativhypothese H_A = mü < mü_0
# 3. Verteilung N(70, (1.5^2/12))
# 4. Signifikanzniveau alpha = 5%
# 5. Verwerfungsbereich

std = 1.5

p = norm.ppf(q=0.05, loc=70, scale=(std)/np.sqrt(12))
# In Python die Standardabweichung nicht hoch 2?
# Ja denn wir rechnen auch mit sqrt(n). Ist Python spezifisch...
# 69.28775748677653

# 6. Testentscheid

m = wf.mean() # 70.25


##################################################

# AUFGABE 6.2

##################################################


# Gleicher Vorgang, nur dass wir Standardabweichung
# aus den Daten ermitteln und nun den t-Test verwenden

# 1. Geschätzte Standardabweichung (Model)
wf = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
std = wf.std() # 1.9598237397554634

# 2. Nullhypothese H_0: 70
# 3. Verteilung = t-Verteilung mit n - 1 = 12 - 1 = 11 Freiheitsgraden
# 4. Signifikanzniveau = 5%
# 5. Teststatistik
p = t.ppf(q=0.05, df=11, loc=70, scale=std/np.sqrt(12))
# 68.98397388627933

# 6. Testentscheid
m = wf.mean() # 70.25


##################################################

# AUFGABE 6.3

##################################################


# a.) ---
# 1. Model, 10^2mcg
# 2. Nullhypothese H_0: 200
#    Alternativhypothese H_A: mü > 200
# 3. Verteilung (z-Verteilung): N(200, 10^2/16)
# 4. Signifikanzniveau 5%
# 5. Teststatistik (wieso 0.95?)
p = norm.ppf(q=0.95, loc=200, scale=10/np.sqrt(16))
# 204.1121340673787

# 6. Testentscheid
204.1121340673787

# Nullhypothese wird verworfen, Grenzüberschreitung

# b.) ---
p = 1 - norm.cdf(x=204.11, loc=205, scale=10/np.sqrt(16))
# 0.6390797174095532

# c.) ---
# Genau das Niveau des Tests (5%)

# d.) ---
p = t.ppf(q=0.95, df=15, loc=200, scale=10/np.sqrt(16))
# 204.38262588923138

# Wieso kann jetzt nicht verworfen werden?

