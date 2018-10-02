
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
#input_dir='C:/Users/11307/Documents/python/paper/files/'
#save_dir='C:/Users/11307/Documents/python/paper/figures/'
###############
df=read_csv(input_dir+'site.csv')
Lat=df["Latitude"]
Lon=df["Longitude"]
index=df.icol(0)
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
for i in range(len(x)):
    plt.text(x[i], y[i],index[i],fontsize=10,fontweight='bold', ha='center',va='center',color='black')
my_map.plot(x, y, 'ro', markersize=12)
a.set_title('Multi-year FSRS catch & temp sites',fontsize=20)
my_map.drawparallels(np.arange(40,80,0.5),labels=[1,0,0,1])
my_map.drawmeridians(np.arange(-180,180,0.5),labels=[1,1,0,1])
plt.savefig(save_dir+'sites_map',dpi=200)
plt.show()
