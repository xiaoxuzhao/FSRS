# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:12:00 2018

@author: xiaoxuzhao
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

################
input_dir='/home/zdong/xiaoxu/paper/file/'
save_dir='/home/zdong/xiaoxu/paper/figure/'
###############
df=read_csv(input_dir+'remove_bad_temperature.csv')
Date=df["eventDate"]
Lat=df["decimalLatitude"]
Lon=df["decimalLongitude"]
info=df["dynamicProperties"]
count=df["individualCount"]
Depth=df["depth"]
fig = plt.figure()
a=fig.add_subplot(1,1,1)
my_map = Basemap(projection='merc', lat_0 = 43, lon_0 = -64,
    resolution = 'h', area_thresh = 0.3,
    llcrnrlon=-68.5, llcrnrlat=41.9,
    urcrnrlon=-57.5, urcrnrlat=48.1) 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'grey')
my_map.drawmapboundary()
x,y=my_map(df["decimalLongitude"].values,df["decimalLatitude"].values)
my_map.plot(x, y, 'bo', markersize=6)
a.set_title('the station of the lobster trap hauls',fontsize=20)
my_map.drawparallels(np.arange(40,80,2),labels=[1,0,0,1])
my_map.drawmeridians(np.arange(-180,180,2),labels=[1,1,0,1])
plt.savefig(save_dir+'station_good_data',dpi=200)
plt.show()
