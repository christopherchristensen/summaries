#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:52:43 2018

@author: Christopher
"""

import pandas as pd
from pandas import DataFrame, Series
fuel = pd.read_table(r"d.fuel.dat", sep=",", index_col=0)