#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 07:52:31 2019

@author: cj
"""
import numpy as np
import pandas as pd
import scipy.stats as st


# =============================================================================
# 3a
# =============================================================================

gamma = pd.read_table(r"./gamma2.txt", delim_whitespace=True)

gamma.describe()

s_xn  = (gamma.std() / np.sqrt(gamma.size))[0]
rel   = s_xn / gamma.mean()[0] / np.sqrt(gamma.size)
rel_p = rel * 100

x_n   = (gamma.mean()[0] / np.sqrt(gamma.size))

st.t.cdf(x=gamma.mean()[0], loc=1, scale=s_xn, df=gamma.size-1) * 2


# =============================================================================
# 6
# =============================================================================
schoko = pd.read_table(r"Schokolade_Nobelpreis.txt", delim_whitespace=True)
schoko.corr()

