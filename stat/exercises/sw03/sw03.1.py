#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:40:56 2019

@author: christopher
"""

import pandas as pd
import scipy.stats as st


# =============================================================================
# 3.4
# =============================================================================

# Durch Python
st.norm.cdf(x=40, loc=32, scale=6)
# Durch Standardisieren
st.norm.cdf(1.33333)


# Durch Python
st.norm.cdf(x=27, loc=32, scale=6)
# Durch Standardisieren
st.norm.cdf(x=-0.83333)


# Durch Python
st.norm.ppf(q=0.975, loc=32, scale=6)

# Durch Standardisieren
z = st.norm.ppf(q=0.975)
x = z * 6 + 32
x

# Durch Python
st.norm.ppf(q=0.1, loc=32, scale=6)
# Durch Standardisieren
z = st.norm.ppf(q=0.1)
x = z * 6 + 32
x


# Durch Python
st.norm.cdf(x=38, loc=32, scale=6) - st.norm.cdf(x=26, loc=32, scale=6)


# =============================================================================
# 3.5
# =============================================================================

1 - st.norm.cdf(x=0.9, loc=0, scale=0.45)
1 - st.norm.cdf(x=2)


st.norm.ppf(q=[0.005, 0.995], loc=0, scale=0.45)
st.norm.cdf(x=0.9, loc=1.8, scale=0.45)


# =============================================================================
# 3.6
# =============================================================================
p = st.norm.cdf(x=[0.25-0.0015, 0.25+0.0015], loc=0.2508, scale=0.0005)
p[1] - p[0]

p = st.norm.cdf(x=[0.25-0.0015, 0.25+0.0015], loc=0.2500, scale=0.0005)
p[1] - p[0]