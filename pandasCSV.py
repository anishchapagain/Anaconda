# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 19:24:08 2016
@author: peter
"""

import csv
import pandas as pd
import sys

## Open the earthquake data file.
data = pd.read_csv('sample/earthquakeGorkha_aftershocks_test1.csv')
lats,lons = [], []
epicentre,magnitudes = [],[]
timestrings = []

val = sys.argv[1]
print("Command %s \n" % val)
command=val.split('-')

if command[0]=='mag':
    column='emagnitude'
    if command[1]=='lt':
        reader = data[data[column]<=float(command[2])]
    elif command[1]=='gt':
        reader = data[data[column]>=float(command[2])]
    else:
        print("\n Please input Correct format 'mag-lt-6'")

print("Total Rows : %s , Matched : %s\n" % (len(data),len(reader)))

for index,row in reader.iterrows():
    lats.append(float(row['elatitude']))
    lons.append(float(row['elongitude']))
    epicentre.append(row['epicentre'])
    magnitudes.append(float(row['emagnitude']))
    timestrings.append(row['edate']+" "+row['etime'])