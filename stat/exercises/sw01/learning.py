# -*- coding: utf-8 -*-

from pandas import Series
import pandas as pd

methodeA = Series([79.87, 30.23, 40.09, 80.04, 80.02, 80.04, 80.03,
80.03, 80.04, 79.97, 80.05, 80.03, 80.02, 80.00, 80.02])

print(methodeA.mean());

print(((2-4)+(6-4)+(3-4)+(5-4)) /4)

# Varianz und Standardabweichung zweier Datensätze
seriesDataSetA = Series([2, 6, 3, 5])

print(seriesDataSetA.var())
print(seriesDataSetA.std())

seriesDataSetA = Series([4, 4, 4, 4])

print(seriesDataSetA.var())
print(seriesDataSetA.std())