# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:25:46 2018

@author: xiaoxu zhao
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

################
input_dir='/home/zdong/xiaoxu/paper/file/'
save_dir='/home/zdong/xiaoxu/paper/figure/'
file='sites_good_depth.csv'
#input_dir='C:/Users/11307/Documents/python/paper/files/'
#save_dir='C:/Users/11307/Documents/python/paper/figures/'
###############
df=read_csv(input_dir+file)
Lat=df["Latitude"]
Lon=df["Longitude"]
fig = plt.figure()
a=fig.add_subplot(1,1,1)
my_map = Basemap(projection='merc', 
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-66.5, llcrnrlat=43.0,
    urcrnrlon=-64.0, urcrnrlat=44.5) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'grey')
my_map.drawmapboundary()
x,y=my_map(df["Longitude"].values,df["Latitude"].values)
my_map.plot(x, y, 'ro', markersize=8)
a.set_title('the sites of the lobster trap hauls',fontsize=20)
my_map.drawparallels(np.arange(40,80,0.5),labels=[1,0,0,1])
my_map.drawmeridians(np.arange(-180,180,0.5),labels=[1,1,0,1])
plt.savefig(save_dir+'sites_map_good_depth',dpi=200)
plt.show()
