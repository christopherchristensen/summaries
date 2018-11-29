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

# AUFGABE 7.1

##################################################

p = t.interval(alpha=0.95, df=8, loc=4, scale=2/np.sqrt(9))