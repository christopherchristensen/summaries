#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 07:13:56 2019

@author: christopher
"""
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

from pandas import DataFrame, Series


# =============================================================================
# 8.1
# =============================================================================

x = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
st.probplot(x, plot=plt)

x_vz = x[x.mean() < x]
st.binom_test(x=x_vz.size, n=x.size, p=0.5, alternative="less")

st.wilcoxon(x=x-70, zero_method="wilcox", correction=True)
1 - 0.6902117434795202/2



# =============================================================================
# 8.3
# =============================================================================

st.t.ppf(q=0.05, loc=0, scale=6.2/np.sqrt(9), df=8)



# =============================================================================
# 8.4
# =============================================================================
z = Series([16.3, 12.7, 14.0, 53.3, 117, 62.6, 27.6])
b = Series([10.4, 8.91, 11.7, 29.9, 46.3, 25.0, 29.4])
d = z - b

d_mean = d.mean()
d_std = d.std()

st.ttest_ind(z, b, equal_var=False)
st.mannwhitneyu(z, b, alternative="greater")