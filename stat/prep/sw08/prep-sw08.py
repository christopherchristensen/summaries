#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 15:39:11 2019

@author: christopher
"""

import scipy.stats as st
import numpy as np
import pandas as pd
from pandas import Series

# --- 8.1

wein = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
wein_binom = st.binom_test(x=7, n=wein.size, p=0.5, alternative="less")

wein_binom = st.binom_test(x=7, n=wein.size, p=0.5, alternative="two-sided")
wein_wilcox = st.wilcoxon(wein-70, zero_method="wilcox", correction=True)



# --- 8.2
methodeA = Series([120, 265, 157, 187, 219, 288, 156, 205, 163])
methodeB = Series([127, 281, 160, 185, 220, 298, 167, 203, 171])

st.t.ppf(q=0.05, loc=0, scale=6.2/np.sqrt(9), df=8)


# --- 8.4
jackals = pd.read_table(r"jackals.txt", sep = " ")
jackals
st.ttest_ind(jackals["M"], jackals["W"], equal_var=False)

st.mannwhitneyu(jackals["M"], jackals["W"], alternative = "two-sided")


# --- 8.5
zurich = Series([16.3, 12.7, 14.0, 53.3, 117, 62.6, 27.6])
basel = Series([10.4, 8.91, 11.7, 29.9, 46.3, 25.0, 29.4])

diff = zurich - basel
diff_mean = diff.mean()
diff_std = diff.std()

st.ttest_ind(zurich,basel, equal_var=False)


st.mannwhitneyu(zurich, basel, alternative="greater")