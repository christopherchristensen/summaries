#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:07:34 2018

@author: christopher
"""
import numpy as np

H = np.array([
     [1/np.sqrt(2) - 1, 0, 1, 0],
     [-1, 1/np.sqrt(2), -1, 0],
     [0, 0, 1/np.sqrt(2), 0],
     [0, 0, 0, 1/np.sqrt(2)],
    ])

A = H * [5, 12, 1, 1]