#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:24:23 2019

@author: cj
"""

import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series

# =============================================================================
# 03a
# =============================================================================
gamma = pd.read_csv(r'gamma2.txt', delim_whitespace=True).iloc[:, 1]
gamma_sf = gamma.std() / np.sqrt(gamma.size)
gamma_rel = gamma_sf / gamma.mean() * 100

# =============================================================================
# 03b
# =============================================================================
st.t.cdf(x=gamma.mean(), loc=1, scale=gamma_sf, df=gamma.size-1)

# =============================================================================
# 03c
# =============================================================================
st.t.ppf(q=0.99, loc=gamma.mean(), scale=gamma_sf, df=gamma.size-1)
