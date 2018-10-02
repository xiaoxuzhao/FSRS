# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:40:00 2018
match catch
@author: xiaoxu zhao
"""
from pandas import read_csv
import re
import pandas as pd
#####################
#HARDCODES
#input_dir='C:/Users/11307/Documents/python/getfsrs/all files/'
#save_dir='C:/Users/11307/Documents/python/getfsrs/pictures/'
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
#s=5
#index_mt3=[1,16,73,97,145,216,250,329,369,418]
#####################
df=read_csv(input_dir+'355c0671cde98eb5386b570c663fc7327e374d77.csv')
dfh=read_csv(input_dir+'merge_date_good_depth.csv')
lat=dfh["Latitude"]
lon=dfh["Longitude"]
date=dfh["Date"]
depth=dfh["Depth"]
temp=dfh["Mean_temp"]
Date=df["eventDate"]
Lat=df["decimalLatitude"]
Lon=df["decimalLongitude"]
info=df["dynamicProperties"]
count=df["individualCount"]
Depth=df["depth"]
print len(depth)
date=[i[0:10] for i in date]   #extract date 2002-12-25 00:45:03.0
Date=[i[0:10] for i in Date]   #extract date 2014-02-18 12:00:00
temp=[str(i)[36:62] for i in info]   #extract  Bottom temperature=1.01C;,SampleSize=Trap deployed for 8 days; Bottom temperature=1.01C;
a=[re.findall(r"[-+]?\d*\.\d+|\d+", i) for i in temp] #extract temp number
T=[str(i) for i in a]
lat=[round(i,2) for i in lat]   
lon=[round(i,2) for i in lon]
I,temperature,Catch=[],[],[]
d=0
"""
for i in range(len(lat)):#len(lat)
    a=0
    for s in range(len(Lat)):
        if lat[i]==Lat[s] and lon[i]==Lon[s] and date[i]==Date[s] and int(depth[i])==int(Depth[s]):
            a=s
            I.append(s)
            temperature.append(T[s])
            Catch.append(count[s])
            d+=1
    if a==0:
         I.append(None)
         temperature.append(None)
         Catch.append(None)
print d 
min_start_time=pd.Series(temperature)
dfh['temperature'] = min_start_time
max_end_time=pd.Series(Catch)
dfh['Catch'] = max_end_time
dfh.to_csv(input_dir+'Match_catch_good_depth.csv')
""" 

