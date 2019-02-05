#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:35:34 2019

@author: christopher
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt 
from scipy.stats import uniform



x = np.loadtxt(r"oldfaithful.txt").astype(int)
n = np.mean(x)
nboot = 1000.0
tmpdata = np.random.choice(x, n*nboot, replace=True) 
bootstrapsample = np.reshape(tmpdata, (n, nboot)) 
xbarstar = np.mean(bootstrapsample, axis=0)


d = np.percentile(xbarstar, q=[2.5, 97.5])
print('Vertrauensintervall: ',d)


n = np.median(x)
nboot = 1000.0

tmpdata = np.random.choice(x, n*nboot, replace=True) 
bootstrapsample = np.reshape(tmpdata, (n, nboot)) 
xbarstar = np.median(bootstrapsample, axis=0)

d = np.percentile(xbarstar, q=[2.5, 97.5])

st.norm.ppf(q=0.975)

st.norm.interval(alpha=0.99, loc=31, scale=6/np.sqrt(10))

st.norm.ppf(q=0.995)

st.t.ppf(q=0.975, df=8)

st.t.cdf(x=-400, df=8, loc=-403, scale=3.127/np.sqrt(9))

