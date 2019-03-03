#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 08:53:45 2019

@author: christopher
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

array = Series(np.linspace(0.5, 20, 11))
array.count()

array = Series(np.arange(1, 20, 0.99))
array

mort = DataFrame({
    "wine": ([2.8, 3.2, 3.2, 3.4, 4.3, 4.9, 5.1, 5.2, 5.9,
              5.9, 6.6, 8.3, 12.6, 15.1, 25.1, 33.1, 75.9, 75.9]), 
    "mor": ([6.2, 9.0, 7.1, 6.8, 10.2, 7.8, 9.3, 5.9, 8.9,
             5.5, 7.1, 9.1, 5.1, 4.7, 4.7, 3.1, 3.2, 2.1]) 
})

mort.plot(kind="scatter", x="wine", y="mor")
plt.xlabel("Weinkonsum (Liter pro Jahr und Person)") 
plt.ylabel("Mortalitaet")
plt.show()

x = [5,6,7,8,9]
plt.plot(x=4, y=4*x, c="orange")

plt.show()