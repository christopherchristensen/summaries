#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:39:33 2019

@author: christopher
"""

import pandas as pd
import scipy.stats as st

from scipy.stats import norm

# =============================================================================
# 3.4
# =============================================================================

# EW(X) = 32ppb
# std = 6ppb

p1 = norm.cdf(38, loc=32, scale=6) - norm.cdf(26, loc=32, scale=6)
print(p1)

p2 = norm.cdf(40, loc=32, scale=6)
print(p2)

Z1 = (40 - 32) / 6
p3 = norm.cdf(Z1)
print(p2 == p3)

p4 = norm.cdf(27, loc=32, scale=6)
print(p4)

ppb1 = norm.ppf(0.975, loc=32, scale=6)
print(ppb1)

Z2 = norm.ppf(0.975)
ppb2 = Z2 * 6 + 32
print(ppb2)

ppb3 = norm.ppf(0.1, loc=32, scale=6)
print(ppb3)

Z3 = norm.ppf(0.1)
ppb4 = Z3 * 6 + 32
print(ppb4)

p = norm.cdf([26, 38], loc=32, scale=6)
p = p[1] - p[0]


# =============================================================================
# 3.5
# =============================================================================

# EW(X) = 0 V
# std = 0.45 V
# Bei >0.9 V wird eine 1 detektiert

p5 = 1 - norm.cdf(0.9, loc=0, scale=0.45)
print(p5)

interval1 = norm.ppf([0.005, 0.995], loc=0, scale=0.45)
print(interval1)

p6 = norm.cdf(0.9, loc=1.8, scale=0.45)
print(p6)


# =============================================================================
# 3.6
# =============================================================================

# EW(X) = 0.2508 mm
# std = 0.0005 mm
# Technischen Angaben: 0.2500 +- 0.0015 mm

p7 = norm.cdf([0.2485, 0.2515], loc=0.2508, scale=0.0005)
p7 = p7[1] - p7[0]
print(p7)

p8 = norm.cdf([0.2485, 0.2515], loc=0.2500, scale=0.0005)
p8 = p8[1] - p8[0]
print(p8)
