#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:13:27 2019

@author: cj
"""

import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series

# =============================================================================
# 01a
# =============================================================================
x = np.loadtxt(r'oldfaithful.txt')
n = x.size
nboot = 1000

tmpdata = np.random.choice(x, n*nboot, replace=True)
bootstrapsample = np.reshape(tmpdata, (n, np.int(nboot)))

xbarstar = np.mean(bootstrapsample, axis=0)

d = np.percentile(xbarstar, q=[2.5, 97.5])
print('Vertrauensintervall: ', d)

# =============================================================================
# 01b
# =============================================================================
np.median(x)
xbarstar_median = np.median(bootstrapsample, axis=0)
d_median = np.percentile(xbarstar, q=[2.5, 97.5])
print('Vertrauensintervall: ', d_median)

# =============================================================================
# 01c
# =============================================================================

# ??

# =============================================================================
# 02
# =============================================================================
