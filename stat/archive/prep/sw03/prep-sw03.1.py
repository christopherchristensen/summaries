#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:28:05 2019

@author: christopher
"""

import pandas as pd
import scipy.stats as st

st.norm.cdf(x=40, loc=32, scale=6) # 90.88 %
st.norm.cdf(x=1.33333333333) # 90.88

st.norm.cdf(x=27, loc=32, scale=6) # 20.23 %

st.norm.ppf(q=0.975, loc=32, scale=6) # 40.78 ppb
st.norm.ppf(q=0.1, loc=32, scale=6) # 24.31 ppb


1 - st.norm.cdf(x=0.9, loc=0, scale=0.45)

Z = (0.9 - 0) / 0.45

1 - st.norm.cdf(Z)

q1, q2 = st.norm.ppf(q=[0.005, 0.995], loc=0, scale=0.45)

st.norm.cdf(x=0.9, loc=1.8, scale=0.45)

st.norm.cdf(x=0.2515, loc=0.2508, scale=0.0005) - st.norm.cdf(x=0.2485, loc=0.2508, scale=0.0005)