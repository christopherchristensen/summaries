#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:06:27 2019

@author: christopher
"""

import numpy as np
from pandas import DataFrame
from statsmodels.formula.api import ols

df = DataFrame({
    "Treatment": np.repeat(["Kommerziell", "Vakuum", "Gemischt", "CO2"], 3),
    "steak_id": [7.66, 6.98, 7.80, 5.26, 5.44, 5.80, 7.41, 7.33, 7.04, 3.51, 2.91, 3.66]
})

fit = ols("steak_id~Treatment", data=df).fit()
fit.summary()

# Der Output für CO2 ist nicht sichtbar
# er ist aber gleich 0, denn er gilt als
# Referenz für die anderen Gruppen
# Der Mittelwert von CO2 ist gleich 3.36,
# Die anderen Mittelwerte variieren um 
# diesen Mittelwert (Gemisch = 3.36 + 3.90 = 7.26)
fit.params