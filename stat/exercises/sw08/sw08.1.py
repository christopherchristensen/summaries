#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:11:50 2019

@author: cj
"""
import numpy as np
import pandas as pd
import scipy.stats as st
from pandas import Series, DataFrame

# =============================================================================
# 8.1
# =============================================================================

# a.) Vorzeichentest
wein1   = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
wein1_m = wein1.mean()
wein1_v = wein1.loc[wein1 > wein1.mean()]

st.binom_test(x=wein1_v.size, n=wein1.size, p=0.5, alternative="less")
## Nullhypothese nicht verworfen

# b.) Wilcoxon-Test
st.wilcoxon(wein1-70, correction=True)
## Nullhypothese nicht verworfen

# =============================================================================
# 8.3
# =============================================================================
diff = Series([-7, -16, -3, 2, -1, -10, -11, 2, -8])
data1 = Series([120, 265, 157, 187,219,288,156,205,163])
data2 = Series([127, 281, 160, 185, 220, 298, 167, 203, 171])


st.ttest_rel(data1, data2)
st.t.ppf(q=0.05, loc=0, scale=6.2/np.sqrt(diff.size), df=diff.size-1)
# Nullhypothese verworfen

# =============================================================================
# 8.4
# =============================================================================
jackals = pd.read_csv(r"jackals.txt", sep = " ")
st.ttest_ind(jackals['M'], jackals['W'], equal_var=False)


# =============================================================================
# 8.5
# =============================================================================
st.mannwhitneyu(jackals["M"], jackals["W"], alternative = "two-sided")

# =============================================================================
# 8.6
# =============================================================================

mdma = DataFrame({
    'Zürich': [16.3, 12.7, 14.0, 53.3, 117, 62.6, 27.6],
    'Basel': [10.4, 8.91, 11.7, 29.9, 46.3, 25.0, 29.4]
})

d = mdma['Zürich'] - mdma['Basel']
d_mean = d.mean()
d_std = d.std()

# Annahme: ist normalverteilt, deswegen ist t-Test möglich! Ansonsten Mannwhitneyu.
d_int = st.t.interval(alpha=0.05, df=d.size, loc=0, scale=d_std / np.sqrt(d.size))

# Da Daten ungepaart wählen wir ttest_ind und nicht st.t.cdf...
st.ttest_ind(mdma['Zürich'], mdma['Basel'], equal_var=False)

# Annahme: nicht normalverteilt, deswegen Mannwhitneyu
st.mannwhitneyu(mdma['Zürich'], mdma['Basel'], alternative='greater').pvalue
