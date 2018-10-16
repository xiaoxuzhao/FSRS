# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:27:50 2018

@author: xiaoxu zhao
"""
from pandas import read_csv
import numpy as np
from pandas import DataFrame
import pdb   #pdb.set_trace()
import operator
##########################
#HARDCODES
input_dir='/home/zdong/xiaoxu/paper/file/'#Xiaoxu's machine
file="site.csv"#program called remove_bad_temperature.py
fil="Mean_count.csv"
##########################
dfh=read_csv(input_dir+file)
df=read_csv(input_dir+fil)  
indexs=dfh["Indexs"]
lat=df['Latitude']   #get the column of latitude
lon=df['Longitude']  #get the column of longitude
date=df['Date']
depth=df['Depth']
mean_count=df['Mean_count']
max_count=df['Max_count']
min_count=df['Min_count']
temperature=df['Temperature']
Lat,Lon,Date,Depth,Temp,Min_count,Max_count,Mean_count=[],[],[],[],[],[],[],[]
indexs=list(indexs)
index_site=reduce(operator.concat, indexs)
index_site=index_site.replace("][",", ")
index_site=index_site.replace("[","")
index_site=index_site.replace("]","")
index_site=index_site.replace(",","")
index_site=index_site.split() 
index_site=[int(i) for i in index_site]
for i in index_site:
    Lat.append(lat[i])
    Lon.append(lon[i])
    Date.append(date[i])
    Depth.append(depth[i])
    Mean_count.append(mean_count[i])
    Max_count.append(max_count[i])
    Min_count.append(min_count[i])
    Temp.append(temperature[i])
site=[]
for i in range(300):
    site.append(1)
for i in range(334):
    site.append(2)
for i in range(205):
    site.append(3)
for i in range(206):
    site.append(4)
for i in range(361):
    site.append(5)
for i in range(357):
    site.append(6)
for i in range(379):
    site.append(7)
for i in range(211):
    site.append(8)
for i in range(201):
    site.append(9)
for i in range(244):
    site.append(10)
data={'Date':np.array(Date),'Latitude':np.array(Lat),
'Longitude':np.array(Lon),'Depth':np.array(Depth),
'Temperature':np.array(Temp),'Mean_count':np.array(Mean_count),'Min_count':np.array(Min_count),
'Max_count':np.array(Max_count),'Site':np.array(site)}
frame=DataFrame(data,columns=['Site','Latitude','Longitude','Date',
                              'Depth','Mean_count','Max_count','Min_count',
                              'Temperature'])                             
frame.to_csv(input_dir+"site_with_station.csv")
