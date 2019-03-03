#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 08:17:59 2019

@author: christopher
"""

import scipy.stats as st

# =============================================================================
# 3.4
# =============================================================================
st.norm.cdf(x=40, loc=32, scale=6)
st.norm.cdf(x=1.33333333333333333)
st.norm.cdf(x=38, loc=32, scale=6) - st.norm.cdf(x=26, loc=32, scale=6)
st.norm.ppf(q=0.975)


# =============================================================================
# 3.5
# =============================================================================
1 - st.norm.cdf(x=0.9, loc=0, scale=0.45)
st.norm.ppf(q=[0.005, 0.995], loc=0, scale=0.45)


st.norm.cdf(x=1, loc=1.8, scale=0.45)

st.norm.cdf(x=0.2515, loc=0.25, scale=0.0005) - st.norm.cdf(x=0.2485, loc=0.25, scale=0.0005)