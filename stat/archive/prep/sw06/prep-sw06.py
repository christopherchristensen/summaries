#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:45:52 2019

@author: christopher
"""

import numpy as np
import scipy.stats as st
from pandas import Series


# --- 6.1

wein = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
wein_Xn = wein.mean()
wein_Z1 = (wein_Xn - 70) / (1.5 / np.sqrt(12))

wein_Z2 = st.norm.cdf(x=wein_Xn, loc=70, scale=1.5/np.sqrt(12))



# --- 6.2

wein2 = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
wein2_Xn2 = wein2.mean()
wein2_Z1 = (wein2_Xn2 - 70) / 1.96 / np.sqrt(12)
wein2_Z2 = st.t.ppf(q=0.05, df=11, loc=70, scale=1.96/np.sqrt(12))


# --- 6.3

vb = st.norm.ppf(q=0.95, loc=200, scale=10/np.sqrt(16))


ws_205 = 1 - st.norm.cdf(x=204.11, loc=205, scale=10/np.sqrt(16))

Z = st.t.ppf(q=0.95, df=16-1, loc=200, scale=10/np.sqrt(16))