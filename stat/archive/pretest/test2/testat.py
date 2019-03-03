#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:09:22 2018

@author: christopher
"""
import numpy as np
import pandas as pd
from scipy.stats import t

frame = pd.read_table("./gamma.txt", delim_whitespace=True)["gamma"]

frame.describe()

f = frame.std() / np.sqrt(frame.size) / frame.mean()


# T-Test
std = frame.std()
# ha = 0
# a = 0.05

pWert = t.ppf(q=0.05, df=frame.size-1, loc=frame.mean(), scale=std/np.sqrt(frame.size))

mean = frame.mean()

schoko = pd.read_table("./Schokolade_Nobelpreis.txt", delim_whitespace=True)

schoko.describe()

corr = schoko.corr() # 0.75859