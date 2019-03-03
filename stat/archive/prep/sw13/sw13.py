#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:26:19 2019

@author: christopher
"""

import matplotlib.pyplot as plt 
import pandas as pd
from pandas import DataFrame 
import numpy as np
from scipy.stats import norm 
import scipy.stats as st


sp2012 = pd.read_table('./sp2012.txt') 

df = DataFrame(sp2012)

plt.plot(df)
plt.xlabel("Zeit (Tage)") 
plt.ylabel("Wert")
plt.title('S&P 500 - Aktienkurs 2012') 
plt.show()


# pd.norm.rvs(size=1257.6, loc=0.483, scale=11)



#steps = np.array(norm.rvs(size=1257.6, loc=0.483, scale=11)) 
#sp_simulated = np.empty([250]) 
# sp_simulated[0] = 

#for i in range(249):
#    sp_simulated[i+1] = sp_simulated[i]+ steps[i]
    
#plt.plot(sp_simulated) 
#plt.xlabel("...") 
#plt.ylabel("...") 
#plt.title('...') 
#plt.show()

p = 1 - norm.cdf(x=1, loc=5, scale=2)

st.norm.cdf(x=10*(np.e**(1/2)))