# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:10:07 2018

@author: 11307
"""

from pandas import read_csv
import numpy as np
from pandas import DataFrame
import pdb
from dateutil.parser import parse
from datetime import datetime
import datetime
##########################
#HARDCODES
input_dir='/home/zdong/xiaoxu/paper/file/'#Xiaoxu's machine
#input_dir='C:/Users/11307/Documents/python/paper/files/'#Xiaoxu's machine
file="site_center.csv"
y=7  #more than 7 years
n=200 #more than 200
ind=[1,2,3,4,5,6,7,8,9,10]
##########################
dfh=read_csv(input_dir+file)     
lat=dfh['Latitude']   #get the column of latitude
lon=dfh['Longitude']  #get the column of longitude
num_row_near=dfh["Num_row_near"]
time=dfh["Time"]
indexs=dfh["Indexs"]
year_num=dfh["Year_num"]
year=dfh["Year"]
Lat,Lon,Num_row_near,Time,Indexs,Year,Year_num=[],[],[],[],[],[],[]
for i in lat.index:
    print i
    if year_num[i]>=y and num_row_near[i]>=n:
        Lat.append(lat[i])
        Lon.append(lon[i])
        Num_row_near.append(num_row_near[i])
        Time.append(time[i])
        Indexs.append(indexs[i])
        Year.append(year[i])
        Year_num.append(year_num[i])
data={'Latitude':np.array(Lat),
'Longitude':np.array(Lon),'Year_num':np.array(Year_num),
'Year':np.array(Year),'Num_row_near':np.array(Num_row_near),
'Time':np.array(Time),'Indexs':np.array(Indexs)}
frame=DataFrame(data,columns=['Latitude','Longitude','Year',
'Year_num','Num_row_near','Time','Indexs'],index=ind)                          
frame.to_csv(input_dir+"site.csv")       