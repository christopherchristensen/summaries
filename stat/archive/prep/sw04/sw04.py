#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 11:28:12 2019

@author: christopher
"""
import matplotlib.pyplot as plt 
from scipy.stats import norm 
import numpy as np
from pandas import Series
import scipy.stats as st



# =============================================================================
# 4.2
# =============================================================================

n=5
m = 500
ran = np.array(norm.rvs(size=n*m)) 
sim = ran.reshape((n,m))

plt.plot(sim)

sim_mean = Series(sim.mean(axis=0))
sim_mean.plot(kind="hist", edgecolor="black")

plt.hist(sim.T,edgecolor="black")



# =============================================================================
# 4.3
# =============================================================================

norm.cdf(x=95, loc=100, scale=10/np.sqrt(25))

# N(5, 4/12)



# =============================================================================
# 4.4
# =============================================================================

norm.cdf(x=2, loc=1, scale=2) - norm.cdf(x=0, loc=1, scale=2)
norm.cdf(x=51, loc=50, scale=np.sqrt(200)) - norm.cdf(x=49, loc=50, scale=np.sqrt(200))
norm.cdf(x=2, loc=1, scale=np.sqrt(4/50)) - norm.cdf(x=0, loc=1, scale=np.sqrt(4/50))



# =============================================================================
# 4.5
# =============================================================================
a = Series([79.98, 80.04, 80.02, 80.04, 80.03, 80.03, 80.04, 79.97, 80.05, 
            80.03, 80.02, 80.00, 80.02])

b = Series([80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 79.97])

mean_a = a.sum() / a.size
mean_b = b.sum() / b.size

var_a = ((a - mean_a)**2).sum() / (a.size-1)
var_b = ((b - mean_b)**2).sum() / (b.size-1)

a.var()
a.std() / np.sqrt(a.size)

std_a = np.sqrt(var_a)
std_b = np.sqrt(var_b)

abs_a = std_a / np.sqrt(a.size)
abs_b = std_b / np.sqrt(b.size)

# mean_a +- abs_a
# mean_b +- abs_b

rel_a = abs_a / mean_a * 100
rel_b = abs_b / mean_b * 100


x = np.array([24.4, 27.6, 27.8, 27.9, 28.5, 30.1, 30.1, 30.3, 31.7, 32.2, 
              32.8, 33.3, 33.5, 34.1, 34.6, 35.8, 35.9, 36.8, 37.1, 39.2, 39.7])

st.probplot(x, plot=plt)