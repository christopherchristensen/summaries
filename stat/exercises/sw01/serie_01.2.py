#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 18:09:18 2018

@author: Christopher
"""

from pandas import Series,DataFrame 
import pandas as pd

data = pd.read_csv(r"child.csv", sep=",", index_col=0)

data.shape
data.describe()
data.index

print("01.2 d.) : China existiert nicht und die Spaltennamen erhält man als Array")
print("")

data.sort_values(by="Drunkenness", ascending=0)[0:5]["Drunkenness"]

data.nsmallest(1,"Infant.mortality")["Infant.mortality"]

physical_act = data["Physical.activity"]
mean_act     = physical_act.mean()

data.loc[physical_act < mean_act, :].index