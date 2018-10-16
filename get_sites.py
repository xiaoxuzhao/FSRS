# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:50:06 2018

@author: 11307
"""

from pandas import read_csv
import numpy as np
from pandas import DataFrame
import pdb
from math import radians, cos, sin, atan, sqrt
from dateutil.parser import parse
##########################
#HARDCODES
input_dir='/home/zdong/xiaoxu/paper/file/'#Xiaoxu's machine
#input_dir='C:/Users/11307/Documents/python/paper/files/'#Xiaoxu's machine
file="Mean_count.csv"
distance=1
##########################
def haversine(loni, lati, lons, lats):
       """
       Calculate the great circle distance between two points 
       on the earth (specified in decimal degrees)
       """
       loni, lati, lons, lats = map(radians, [loni, lati, lons, lats]) 
       #print 34
       dlon = lons - loni  
       dlat = lats - lati  
       a = sin(dlat/2)**2 + cos(lati) * cos(lats) * sin(dlon/2)**2 
       c = 2 * atan(sqrt(a)/sqrt(1-a))  
       r = 6371
       d=c * r        
       return d
dfh=read_csv(input_dir+file)     
lat=dfh['Latitude']   #get the column of latitude
lon=dfh['Longitude']  #get the column of longitude
date=dfh['Date']
Num_row_near,Indexs,Min_time,Lat,Lon,Max_time,Time=[],[],[],[],[],[],[]
Year,Year_num=[],[]
i=0
while i<=len(lat):#347739
      print i
      num=[]
      time=[]
      year=[]
      for s in lat.index:
          if haversine(lon[i],lat[i],lon[s],lat[s])<distance:
              num.append(s)    #get index of the points which within one kilometer :
              time.append(parse(date[s]))
              year.append(date[s][0:4])
      y=sorted(set(year),key=year.index)
      Year.append(y)
      Year_num.append(len(y))
      Lat.append(lat[i])
      Lon.append(lon[i])
      Num_row_near.append(len(num))    #get the total num of indexs
      Indexs.append(num)
      Min_time.append(min(time))
      Max_time.append(max(time))
      Time.append(max(time)-min(time))
      for d in num:
            del lat[d]
            del lon[d]
      if len(lat)==0:
          break
      else:
          i=lat.index[0]
      #pdb.set_trace()
data={'Year_num':np.array(Year_num),'Year':np.array(Year),'Indexs':np.array(Indexs),'Latitude':np.array(Lat),
'Longitude':np.array(Lon),'Num_row_near':np.array(Num_row_near),
'Min_time':np.array(Min_time),'Max_time':np.array(Max_time),'Time':np.array(Time)}
frame=DataFrame(data,columns=['Latitude','Longitude','Year','Year_num',
                              'Num_row_near','Time','Max_time','Min_time',
                              'Indexs'])                             
frame.to_csv(input_dir+"site_center.csv")