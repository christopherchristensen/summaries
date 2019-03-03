#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:40:54 2019

@author: christopher
"""
import numpy as np
import scipy.stats as st
from pandas import DataFrame, Series



# =============================================================================
# 7.2
# =============================================================================
x = Series(st.uniform.rvs(size=60, loc=0, scale=9))

interval = st.norm.interval(alpha=0.95, loc=5, scale=(10-0)/np.sqrt(12))
e = x.mean() - interval[0]

st.norm.ppf(q=0.975)



# =============================================================================
# 7.3
# =============================================================================
interval = st.norm.interval(alpha=0.99, loc=31, scale=6/np.sqrt(10))

st.norm.ppf(0.005)
st.t.ppf(0.005, df=9)/ st.norm.ppf(0.005)


# =============================================================================
# 7.5
# =============================================================================
y = Series([520, 512, 499, 524, 505])
y.mean()
y.var()

st.t.ppf(q=0.95, loc=500, scale=y.std()/np.sqrt(5), df=4)

st.t.interval(alpha=0.95, loc=512, scale=y.std()/np.sqrt(5), df=4)
st.norm.interval(alpha=0.95, loc=512, scale=y.std()/np.sqrt(5))