# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:10:45 2018

@author: xiaoxu zhao
"""
from pandas import read_csv
import numpy as np
from pandas import DataFrame
#####################
#HARDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/paper/figure/'
file='site_with_station.csv'
num=[1,2,3,4,5,6,7,8,9,10]
#####################
dfh=read_csv(input_dir+file)
index=dfh.icol(1)
depth=dfh["Depth"]
lon=dfh['Longitude']
lat=dfh["Latitude"]
date=dfh['Date']
site=dfh["Site"]
mean_count=dfh["Mean_count"]
max_count=dfh["Max_count"]
min_count=dfh["Min_count"]
temperature=dfh["Temperature"]
Depth,Mean_depth,Good_index,Dep=[],[],[],[]
for i in range(len(num)):
    Depth=[]
    for s in range(len(lat)): 
        if index[s]==num[i]:
             Depth.append(depth[s])  
    Mean_depth.append(np.mean(Depth))
for i in range(len(num)):
   Depth=[]
   for s in range(len(lat)): 
         if index[s]==num[i]:
             Depth.append(depth[s])
   Dep.append(Depth)             
for i in range(len(num)):
   for s in range(len(lat)):
         if index[s]==num[i]:
             if abs(depth[s]-Mean_depth[i])<=np.std(Dep[i],ddof=1):
                 Good_index.append(s)
site=site.loc[Good_index]
lat=lat.loc[Good_index]
lon=lon.loc[Good_index]
date=date.loc[Good_index]
depth=depth.loc[Good_index]
min_count=min_count.loc[Good_index]
max_count=max_count.loc[Good_index]
mean_count=mean_count.loc[Good_index]
temperature=temperature.loc[Good_index]
data={'Site':np.array(site),'Latitude':np.array(lat),
      'Longitude':np.array(lon),'Date':np.array(date),'Depth':np.array(depth),
      'Min_count':np.array(min_count),'Max_count':np.array(max_count),'Mean_count':np.array(mean_count),
      'Temperature':np.array(temperature)}
frame=DataFrame(data,columns=['Site','Latitude','Longitude','Date',
                              'Depth','Min_count','Max_count','Mean_count',
                              'Temperature'])                              
frame.to_csv(input_dir+"sites_good_depth.csv")    
     


