
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 09:50:04 2018
the stations  have the same time obtain the mean catch,min catch,max catch
@author: xiaoxuzhao
"""
from pandas import read_csv
import numpy as np
from pandas import DataFrame
import pdb   #pdb.set_trace()
import re
import pandas as pd
##########################
#HARDCODES
input_dir='/home/zdong/xiaoxu/paper/file/'#Xiaoxu's machine
file="remove_bad_temperature.csv"#program called remove_bad_temperature.py
##########################
dfh=read_csv(input_dir+file)     
lat=dfh['decimalLatitude']   #get the column of latitude
lon=dfh['decimalLongitude']  #get the column of longitude
count=dfh["individualCount"]#lobster catch
info=dfh["dynamicProperties"]#temperature
temp=[str(i)[36:62] for i in info]   #extract  Bottom temperature=1.01C;,SampleSize=Trap deployed for 8 days; Bottom temperature=1.01C;
a=[re.findall(r"[-+]?\d*\.\d+|\d+", i) for i in temp] #extract temp number
t=[str(i) for i in a]
T=pd.Series(t)
date=dfh["eventDate"]
depth=dfh["depth"]
Mean_count=[]
Lat,Lon,Date,Depth,Temp,Min_count,Max_count=[],[],[],[],[],[],[]
i=0
while i<=len(lat):
      print i
      num=[]
      catch=[]
      for s in lat.index:
          if lat[i]==lat[s] and lon[i]==lon[s] and date[i]==date[s] and depth[i]==depth[s] and T[i]==T[s]:
              num.append(s)
              catch.append(count[s])
      Min_count.append(min(catch))
      Max_count.append(max(catch))
      Mean_count.append(np.mean(catch))
      Lon.append(round(lon[i],2))
      Lat.append(round(lat[i],2))
      Date.append(date[i])
      Depth.append(round(depth[i],2))
      Temp.append(T[i])
      for d in num:
            del lat[d]
            del lon[d]
            del date[d]
            del depth[d]
            del T[d]
      if len(lat)==0:
          break
      else:
          i=lat.index[0]
print len(Mean_count),len(Lat),len(Lon),len(Date),len(Depth),len(Min_count),len(Max_count)
data={'Date':np.array(Date),'Latitude':np.array(Lat),
'Longitude':np.array(Lon),'Depth':np.array(Depth),
'temperature':np.array(Temp),'Mean_count':np.array(Mean_count),'Min_count':np.array(Min_count),
'Max_count':np.array(Max_count)}
frame=DataFrame(data,columns=['Latitude','Longitude','Date',
                              'Depth','Mean_count','Max_count','Min_count',
                              'Temperature'])                             
frame.to_csv(input_dir+"Mean_count.csv")

