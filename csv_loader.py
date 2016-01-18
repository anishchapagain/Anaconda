# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 19:24:08 2016
@author: peter
"""

import csv

## Open the earthquake data file.
filename = 'sample/earthquakeGorkha_aftershocks_test1.csv'
#filename = 'NPL_adm_shp/NPL_adm4.csv'

lats,lons = [], []
epicentre,magnitudes = [],[]
timestrings = []

#Read through the entire file, skip the first line, and pull out just the lats and lons.
with open(filename) as f:  ## Create a csv reader object.
    reader = csv.reader(f)    
    next(reader) # Ignore the header row.    
       
    
    for row in reader:
        print(row)
        
#        lats.append(float(row[1]))
#        lons.append(float(row[0]))
#        magnitudes.append(float(row[4]))
#        timestrings.append(row[5])