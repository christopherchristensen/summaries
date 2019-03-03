#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:15:55 2019

@author: christopher
"""

import numpy as np
import pandas as pd
from pandas import DataFrame


mort = DataFrame({
    "wine": ([2.8, 3.2, 3.2, 3.4, 4.3, 4.9, 5.1, 5.2, 5.9, 
              5.9, 6.6, 8.3, 12.6, 15.1, 25.1, 33.1, 75.9, 75.9]), 
    "mor": ([6.2, 9.0, 7.1, 6.8, 10.2, 7.8, 9.3, 5.9, 8.9, 
             5.5, 7.1, 9.1, 5.1, 4.7, 4.7, 3.1, 3.2, 2.1])
})

mort["wine"].size
mort["mor"].size


book = DataFrame({
    "Bücher": ["Buch 1", "Buch 2", "Buch 3", "Buch 4", "Buch 5", 
                         "Buch 6", "Buch 7", "Buch 8", "Buch 9", "Buch 10"],
    "Seitenzahl": [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
    "Buchpreis": [6.4, 9.5, 15.6, 15.1, 17.8, 23.4, 23.4, 22.5, 26.1, 29.1]
})

book.set_index("Bücher", inplace=True)

#     "Details": np.tile(["Seitenzahl", "Buchpreis"], 2),