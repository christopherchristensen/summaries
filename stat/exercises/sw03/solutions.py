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
from scipy.stats import norm
import numpy as np

##################################################

# AUFGABE 3.4

##################################################

# --- Kummulative Verteilungsfunktion
# CDF erstellt eine kummulative Verteilungsfunktion 
# mit den gegebenen Werten. 
# Immer wenn man den "höchstens"-Wert einer uniformen
# Verteilung berechnen müssen, verwendet man norm.cdf.
# x = "höchstens", loc = Erwartungswert
P = norm.cdf(x=40, loc=32, scale=6);