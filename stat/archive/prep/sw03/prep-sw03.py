#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 08:55:36 2019

@author: christopher
"""

# --- 3.4
import scipy.stats as st

# 90.88%
w_40 = st.norm.cdf(x=40, loc=32, scale=6)

# 90.88%
n_40 = st.norm.cdf(x=(40-32)/6)

# 20.23%
w_27 = st.norm.cdf(x=27, loc=32, scale=6)

# 43.76ppb
bg_97d5 = st.norm.ppf(q=0.975, loc=32, scale=6)

# 97.5%
w_43d76 = st.norm.cdf(x=43.759783907240326, loc=32, scale=6)

# 24.31ppb
bg_10 = st.norm.ppf(q=0.1, loc=32, scale=6)

# 68.27%
interval = st.norm.cdf(x=38, loc=32, scale=6) - st.norm.cdf(x=26, loc=32, scale=6)


# --- 3.5

# 2.28%
w1_0d9 = 1 - st.norm.cdf(x=0.9, loc=0, scale=0.45)

# -1.16V
interval_99d5 = st.norm.ppf(q=0.995, loc=0, scale=0.45)

# +1.16V
interval_00d5 = st.norm.ppf(q=0.005, loc=0, scale=0.45)

w2_0d9 = st.norm.cdf(x=0.9, loc=1.8, scale=0.45)


# --- 3.6

# 91.92%
interval1_tA = st.norm.cdf(x=0.25+0.0015, loc=0.2508, scale=0.0005) - st.norm.cdf(x=0.25-0.0015, loc=0.2508, scale=0.0005)

# 99.73%
interval2_tA = st.norm.cdf(x=0.25+0.0015, loc=0.25, scale=0.0005) - st.norm.cdf(x=0.25-0.0015, loc=0.25, scale=0.0005)


# 3.7
from scipy.stats import uniform
import numpy as np

x = uniform.rvs(size=100, loc=-1, scale=2)
w_kreis = 1 - np.pi /4 / np.sum(x<1)