#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:52:43 2018

@author: Christopher
"""

import pandas as pd
from pandas import DataFrame, Series
fuel = pd.read_table(r"d.fuel.dat", sep=",", index_col=0)

fuel.describe

fuel.loc[1]
fuel.loc[1:5]

fuel.mean()["mpg"]
fuel.loc[7:22].mean()["mpg"]

t_kml = fuel["mpg"]*1.61/3.79
t_kml.describe()
t_kml.head()
t_kml.mean()

t_kg = fuel["weight"]*0.45359
t_kg.describe()
t_kg.head()
t_kg.mean()