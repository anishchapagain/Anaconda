# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 20:05:15 2016
26.53  86.73
@author: peter
"""
import pandas as pd

#coumns elongitude,elatitude,epicentre,etime,emagnitude,edate
data = pd.read_csv('sample/earthquakeGorkha_aftershocks_test1.csv')

# get rows from DataFrame: data
reader = data
#reader = data[data['emagnitude']>=4.5 ]
#reader = data[data.epicentre.isin(['Sindhupalchowk','Nuwakot','Gorkha']) & (data.emagnitude>5.0)]
#reader = data[data.epicentre.isin(['Sindhupalchowk','Nuwakot','Gorkha']) ]#Dolakha
#reader = data[data.epicentre.str.contains(r'Dol')]#Dolakha
#reader = data[data.edate.str.contains(r'/04/')] #April
#reader = data[data.edate.between('2015/04/25','2015/04/31') & data.epicentre.str.contains(r'Sindhu')]
#reader = data[data.edate.str.contains(r'/04/') & data.epicentre.str.contains(r'Sindhu')]
print("Total Rows : %s , Matched : %s\n" % (len(data),len(reader))) 

# --- Nepal EarthQuake Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

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
for index,row in reader.iterrows():    #for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = eq_map(float(row['elongitude']),float(row['elatitude']))
    mag= float(row['emagnitude'])
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

plt.title("April-2015 Gorkha Nepal (AfterShocks)")
seven, = plt.plot([1],label='7.0',color='red', marker='D')
six,= plt.plot([1],label='6 - 7',color='yellow',marker='o')
five, = plt.plot([1],label='5 - 6',color='green',marker='^')
four, = plt.plot([1],label='4 - 5',color='blue',marker='o')
plt.legend()
plt.xlabel("Total Rows : %s , Matched : %s\n" % (len(data),len(reader)))
plt.show()