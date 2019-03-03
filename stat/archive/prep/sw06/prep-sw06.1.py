#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:54:54 2019

@author: christopher
"""
import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series

wein = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
wein.describe()
wein_Z = (wein.mean() - 70) / (1.5 / np.sqrt(12))

wein_V = st.norm.ppf(q=0.05)



# --- 6.2
wein2 = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])

wein2_V = st.t.ppf(q=0.05, df=12-1)


# --- 6.3
prob_V = st.norm.ppf(q=0.95)
prob_Ü = 1 - st.norm.cdf(x=204.2, loc=205, scale=10/np.sqrt(16))