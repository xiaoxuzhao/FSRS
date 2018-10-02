# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:34:54 2018

@author: xiaoxu
create file which sites more than somes days
"""

from pandas import read_csv
import numpy as np
from pandas import DataFrame
#####################
#HARDCODES
day=1000
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
#####################
df_fsrs=read_csv(input_dir+'fsrs_sites(>1 km,year).csv')#fsrs_sites(>1 km,year).py
df=read_csv(input_dir+'merge_date_good_depth.csv')    #merge_fsrs.py
df=df.drop_duplicates('Date')
df.to_csv(input_dir+'sort_the_same_date.csv')
df=read_csv(input_dir+'sort_the_same_date.csv')
###################
#get xlim
index_first=list(df.icol(1))
indexs=list(set(index_first))
indexs.sort(key=index_first.index)
depth=df["Depth"]
###################
site,min_depth,max_depth=[],[],[]
for s in range(len(indexs)):
    a=0
    for i in range(len(index_first)):
          if index_first[i]==indexs[s]:
              a+=1
    if (a>day):
        site.append(indexs[s])
Lat,Lon,Event,cru,min_start,max_end,ind=[],[],[],[],[],[],[]
index_sites=df["index_sites"]
lat=df_fsrs["Latitude"]
lon=df_fsrs["Longitude"]
event_spec=df_fsrs["Event_Spec"]
cruise=df_fsrs["Cruise"]
Min_start_time=df_fsrs["min_start_time"]
Num_row_near=df_fsrs["num_row_near"]
Max_end_time=df_fsrs["max_end_time"]
Indexs=df_fsrs["indexs"]
index_fsrs=list(df_fsrs.icol(0))
for s in range(len(site)):
    for i in range(len(index_fsrs)):
        if index_fsrs[i]==site[s]:
            Lat.append(lat[i])
            Lon.append(lon[i])
            Event.append(event_spec[i])
            cru.append(cruise[i])
            min_start.append(Min_start_time[i])
            max_end.append(Max_end_time[i])
            ind.append(Indexs[i])
#print list(ind)[0].replace("[","").replace("]","").split(",")[1]
for i in range(len(site)):#len(site)
    mean_depth=[]
    for s in range(len(list(ind)[i].split(","))):
        print s
        c=0
        de=0
        for d in range(len(index_sites)):
            if index_sites[d]==int(list(ind)[i].replace("[","").replace("]","").split(",")[s]):
                  c+=1
                  de+=depth[d]
        if c>0:
            mean_depth.append(int(de/c))
    #print mean_depth
    min_depth.append(min(mean_depth))
    max_depth.append(max(mean_depth))
data={'Event_spec':np.array(Event),'Cruise':np.array(cru),'Latitude':np.array(Lat),
      'Longitude':np.array(Lon),'Min_start_time':np.array(min_start),'Max_end_time':np.array(max_end),
      'Indexs':np.array(ind),"Min_depth":np.array(min_depth),'Max_depth':np.array(max_depth)}
frame=DataFrame(data,columns=['Event_spec','Cruise','Latitude','Longitude','Min_start_time',
                              'Max_end_time','Indexs','Min_depth','Max_depth'],index=site)                              
frame.to_csv(input_dir+"fsrs_sites("+str(day)+"days_good_depth).csv")

