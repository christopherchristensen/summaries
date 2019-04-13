#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 07:51:21 2019

@author: cj
"""
import numpy as np
import scipy.stats as st
from pandas import Series


# =============================================================================
# 6.1
# =============================================================================

wein   = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
wein_m = wein.mean()

p = st.norm.cdf(wein_m, loc=70, scale=1.5/np.sqrt(wein.size))
s = st.norm.ppf(q=0.05, loc=70, scale=1.5/np.sqrt(wein.size))

# =============================================================================
# 6.2
# =============================================================================

wein2     = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
wein2_m   = wein.mean()
wein2_std = wein2.std()

s2 = st.t.ppf(q=0.05, loc=70, scale=wein2_std/np.sqrt(wein2.size), df=wein2.size-1)
p2 = st.t.cdf(x=wein2_m, loc=70, scale=wein2_std/np.sqrt(wein2.size), df=wein2.size-1)

# =============================================================================
# 6.3
# =============================================================================
nh_m   = 200
nh_std = 10

s3   = st.norm.ppf(q=0.95, loc=nh_m, scale=nh_std/np.sqrt(16))
p3_0 = 1 - st.norm.cdf(x=204.2, loc=nh_m, scale=nh_std/np.sqrt(16))
p3_1 = 1 - st.norm.cdf(x=204.2, loc=205, scale=nh_std/np.sqrt(16))
s4   = st.t.ppf(q=0.95, loc=200, scale=10/np.sqrt(16), df=16-1)