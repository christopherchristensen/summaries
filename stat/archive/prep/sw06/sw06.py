#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:46:14 2019

@author: christopher
"""

import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import DataFrame


# =============================================================================
# 6.1
# =============================================================================
w1 = DataFrame([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])[0]

w1_mean = w1.mean()
st.norm.cdf(x=w1_mean, loc=70, scale=1.5)
st.norm.ppf(q=0.05, loc=70, scale=1.5)



# =============================================================================
# 6.2
# =============================================================================
std = 1.96
st.t.ppf(q=0.05, loc=70, scale=std/np.sqrt(w1.size), df=w1.size-1)



# =============================================================================
# 6.3
# =============================================================================
1 - st.norm.cdf(x=204.2, loc=200, scale=10/np.sqrt(16))
st.norm.ppf(q=0.95, loc=200, scale=10/np.sqrt(16))
1 - st.norm.cdf(x=204.11, loc=205, scale=10/np.sqrt(16))

1 - st.t.cdf(x=204.2, loc=200, scale=10/np.sqrt(16), df=15)

