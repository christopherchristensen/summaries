#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:55:57 2018

@author: Christopher
"""
import pandas as pd
import math
from pandas import DataFrame, Series


x = Series([2.1,2.4,2.8,3.1,4.2,4.9,5.1,6.0,6.4,7.3,10.8,12.5,13.0,13.7,14.8,17.6,19.6, 23.0,25.0,35.2,39.6
])
x.sum()

y = x*x

y.sum()

size = x.size


mean = x.sum() / size
print(mean)

sortX = x.sort_values(0)
print(sortX)
median = sortX.sum() / sortX[math.ceil(sortX.size/2)]

median
print(median)

print(sortX.mean())
print(sortX.std())
print(sortX.median())

upperPercent = sortX[math.ceil(sortX.size * 0.75)]
upperQuantil = sortX.sum() / upperPercent

print("Quantil: ")
print(upperQuantil)
print(sortX.quantile(q=.75, interpolation="midpoint"))

z = (sortX-sortX.mean()) / sortX.std()
print(z.mean())
print(z.std())