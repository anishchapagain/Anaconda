# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 08:44:00 2016

@author: peter
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=79.26, llcrnrlat=26.18,urcrnrlon=88.70, urcrnrlat=30.82, resolution='h', projection='merc')

map.drawmapboundary(fill_color='green')
map.fillcontinents(color='white',lake_color='blue')
map.drawcoastlines()
map.drawcountries(color='b',linewidth=1.0,linestyle='solid')
map.readshapefile('NPL_adm_shp/NPL_adm2', 'Nepal')

plt.show()