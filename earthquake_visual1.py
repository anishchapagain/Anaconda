# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 20:05:15 2016
26.53  86.73
@author: peter
"""

import csv
import sys
#
## Open the earthquake data file.
filename = 'sample/earthquakeGorkha_aftershocks_test1.csv'

## Create empty lists for the data we are interested in.
lats, lons = [], []
magnitudes = []
timestrings = []

#Read through the entire file, skip the first line, and pull out just the lats and lons.
with open(filename) as f:
## Create a csv reader object.
    reader = csv.reader(f)
#    
#    # Ignore the header row.
    next(reader)
#    
#    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[1]))
        lons.append(float(row[0]))
        magnitudes.append(float(row[4]))
        timestrings.append(row[5])
#        
# --- Build Map ---

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def get_marker_color(magnitude):
#    # Returns green for small earthquakes, yellow for moderate
#    #  earthquakes, and red for significant earthquakes.
    if magnitude >= 5.0 and magnitude < 6.0:
        return ('go')
    elif magnitude >= 6.0 and magnitude <7.0:
        return ('yo')
    elif magnitude>= 7.0:
        return ('ro')
    else:
        return ('')

# Make this plot larger.
plt.figure(figsize=(16,12))

# lat_0=26.32, lon_0=86.21,llcrnrlon=82.52, llcrnrlat=26.88,urcrnrlon=81.5, urcrnrlat=30.79
#eq_map = Basemap(projection='merc', resolution = 'h', area_thresh = 10,lat_0=26, lon_0=86,llcrnrlat=26.0,llcrnrlon=86.0,urcrnrlat=26.5,urcrnrlon=86.63)
#eq_map = Basemap(projection='merc', resolution = 'h', area_thresh = 1000,lat_0=26, lon_0=86)
eq_map = Basemap(projection='merc',llcrnrlon=79.26, llcrnrlat=26.18,urcrnrlon=88.70, urcrnrlat=30.82,resolution = 'h')
eq_map.drawcoastlines()
eq_map.drawcountries(color='r',linewidth=2.0,linestyle='solid')
#eq_map.fillcontinents(color = 'gray',)
eq_map.drawmapboundary()
#eq_map.drawrivers(color='#0000ff')
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
 
min_marker_size = 1.0
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = eq_map(lon, lat)
    msize = mag * min_marker_size
    marker_string = get_marker_color(mag)
    eq_map.plot(x, y, marker_string, markersize=msize)
    
title_string = "Earthquakes of Magnitude 5.0 or Greater! April-2015 Gorkha Nepal (AfterShocks)\n"
#title_string += "%s through %s" % (timestrings[-1], timestrings[0])
plt.title(title_string)
 
plt.show()