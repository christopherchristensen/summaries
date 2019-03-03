#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:19:56 2018

@author: christopher
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

x = np.array([24.4, 27.6, 27.8, 27.9, 28.5, 30.1, 30.1, 30.3, 31.7, 32.2, 32.8, 
              33.3, 33.5, 34.1, 34.6, 35.8, 35.9, 36.8, 37.1, 39.2, 39.7])

st.probplot(x, plot=plt)
 

x = st.norm.rvs(size = 2000000)
st.probplot(x, plot = plt)

x = st.uniform.rvs(size=100000)
st.probplot(x, plot = plt)

x = st.chi2.rvs(size=100000, df=20000)
st.probplot(x, plot = plt)


x = 120/15
x = st.expon.cdf(x=12, loc=1/8, scale=8)

