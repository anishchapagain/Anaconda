# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 20:05:15 2016
26.53  86.73
@author: peter
"""
import pandas as pd
import sys

data = pd.read_csv('sample/earthquakeGorkha_aftershocks_test1.csv')
#data = pd.read_csv('sample/earthquakePast.csv')

lats,lons = [], []
epicentre,magnitudes = [],[]
timestrings = []

val = sys.argv[1]
print("Command %s \n" % val)
command=val.split('-')

def get_command(command):
    if command[0]=='mag':
        column='emagnitude'
        if command[1]=='lt':
            readerv = data[data[column]<=float(command[2])]
            return readerv
        elif command[1]=='gt':
            readerv = data[data[column]>=float(command[2])]
            return readerv
    else:
        print("\n Please input Correct format 'mag-lt-6'")
  
reader = get_command(command)
print("Total Rows : %s , Matched : %s\n" % (len(data),len(reader)))
for index,row in reader.iterrows():
    lats.append(float(row['elatitude']))
    lons.append(float(row['elongitude']))
    epicentre.append(row['epicentre'])
    magnitudes.append(float(row['emagnitude']))
    timestrings.append(row['edate']+" "+row['etime'])    

# --- Nepal EarthQuake Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Make this plot larger.
plt.figure(figsize=(20,16))

# lat_0=26.32, lon_0=86.21,llcrnrlon=82.52, llcrnrlat=26.88,urcrnrlon=81.5, urcrnrlat=30.79
eq_map = Basemap(projection='merc',area_thresh = 100,
                 llcrnrlon=79.26, llcrnrlat=26.18,
                 urcrnrlon=88.70, urcrnrlat=30.82,
                 resolution = 'h')
                 
                 
#eq_map.drawcoastlines()
#eq_map.drawcountries(color='r',linewidth=1.0,linestyle='solid')
#eq_map.fillcontinents(color = 'gray',)
eq_map.readshapefile('NPL_adm_shp/NPL_adm2', 'Nepal')
eq_map.drawmapboundary()
#eq_map.drawrivers(color='#0000ff')
#eq_map.drawmeridians(np.arange(0, 360, 30))
#eq_map.drawparallels(np.arange(-90, 90, 30))
 
min_marker_size = 2.50
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = eq_map(lon, lat)
    if mag >= 5.0 and mag < 6.0:
        marker_string = 'g^'
        msize = mag * 1.20
    elif mag >= 6.0 and mag <7.0:
       msize = mag * 1.75
       marker_string ='yo'
    elif mag>= 7.0:
         marker_string ='rD'
         msize = mag * 1.75
    else:
        marker_string ='bo'
        msize = mag * 0.50

    eq_map.plot(x, y, marker_string, markersize=msize)
    
title_string = "Earthquakes of Magnitude %s or Greater! April-2015 Gorkha Nepal (AfterShocks)\n" % command[2]
plt.title(title_string)
seven, = plt.plot([1],label='7.0',color='red', marker='D')
six,= plt.plot([1],label='6 - 7',color='yellow',marker='o')
five, = plt.plot([1],label='5 - 6',color='green',marker='^')
four, = plt.plot([1],label='4 - 5',color='blue',marker='o')
plt.legend()
plt.show()