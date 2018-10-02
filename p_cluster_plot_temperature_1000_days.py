

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:10:37 2018

@author: xiaoxu
"""

#days more than 1000 days
from pandas import read_csv
from dateutil import parser
import matplotlib.pyplot as plt
####################
#HAEDCODES
input_dir='C:/Users/11307/Documents/python/getfsrs/all files/'
save_dir='C:/Users/11307/Documents/python/getfsrs/pictures/'
#input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
#save_dir='/home/zdong/xiaoxu/FSRS/figure/'
s=2
####################
df=read_csv(input_dir+'merge_p_cluster.csv')
dfh=read_csv(input_dir+'p_cluster_sites(_1000days).csv')
index_1000=list(dfh.iloc[:,0])
index_first=list(df.iloc[:,0])
row_index=[]
for i in range(len(index_first)):
    if index_first[i]==index_1000[s]:
            row_index.append(i)
            p=index_1000[s]
df[row_index[0]:row_index[-1]].to_csv(input_dir+str(p)+"_site_sort.csv", index=False)
df=read_csv(input_dir+str(p)+"_site_sort.csv")
df = df.sort_values("Date")
index_sites=df["index_sites"]
date=df["Date"]
Mean_temp=df["Mean_temp"]
depth=df["Depth"]
####################### 
#get unique station value in order
index_sites=df["index_sites"]
index_sites=list(index_sites)
index = list(set(index_sites))
index.sort(key=index_sites.index)
#######################
#Get the first occurrence of the index value
first_appear=[]
for i in range(len(index)):
    q=index_sites.index(index[i])
    first_appear.append(q)
####################### 
#Convert date columns to time format,and only need top ten
Date=[]
for i in date:
          Date.append(parser.parse(i[0:10]))
#######################
fig = plt.figure(figsize=(20,5))
color=["pink","orange","brown","green","black","red","blue","yellow","purple","cyan","magenta","chocolate","beige","lime","tan","fuchsia","cerise"]
for d in range(len(index)):
      a,dep=0,0
      for i in range(len(date)):
           if index_sites[i]==index[d]:
                a+=1
                dep+=depth[i]
      Depth=int(round(dep/a))
      plt.plot(Date[first_appear[d]:first_appear[d]+a], Mean_temp[first_appear[d]:first_appear[d]+a],color=color[d],linewidth=1.5, linestyle="-",label=Depth)

plt.legend(loc='upper left',bbox_to_anchor=(0, 1.0),ncol=4,title="Mean depth(m)")   
plt.title("the site"+str(index_1000[s])+" within 1 kilometer in the coordinates of 44.2652,-66.1663 ")
plt.ylim(0,15)
plt.ylabel(u"Mean temperature (\u2103)")
plt.xlabel('Year')
plt.savefig(save_dir+"p_cluster_"+str(index_1000[s])+" site_ temperature.png")
plt.show()