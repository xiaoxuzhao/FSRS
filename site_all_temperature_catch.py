# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:03:34 2018

@author: xiaoxu zhao
"""
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
from dateutil.parser import parse
from mpl_toolkits.axes_grid1 import host_subplot
#####################
#HARDCODES
#input_dir='C:/Users/11307/Documents/python/paper/files/'
#save_dir='C:/Users/11307/Documents/python/paper/figures/'
input_dir='/home/zdong/xiaoxu/paper/file/'
save_dir='/home/zdong/xiaoxu/paper/figure/'
file='sites_good_depth.csv'
num=[1,2,3,4,5,6,7,8,9,10]
#range(10)
#year='2014'
####################
dfh=read_csv(input_dir+file)
depth=dfh["Depth"]
lon=dfh['Longitude']
lat=dfh["Latitude"]
date=dfh['Date']
site=dfh["Site"]
mean_count=dfh["Mean_count"]
max_count=dfh["Max_count"]
min_count=dfh["Min_count"]
temperature=dfh["Temperature"]
tempe=[]
count=[]
for i in range(10):
    time=[]
    c=[]
    temp=[]
    for s in range(len(site)):
        if site[s]==num[i] :
            time.append(parse(date[s][0:10]))
            a=((temperature[s].replace("[","")).replace(']','')).replace("'","")
            temp.append(a)
    te=[]
    for s in range(len(temp)):
       if temp[s]!='-99.0':
           c.append(s)
           te.append(temp[s])
    te=sorted(te)
    mean_count=mean_count.loc[c]
    tempe.append(te)
    count.append(mean_count)
fig = plt.figure()
a=fig.add_subplot(1,1,1)
plt.plot(tempe[0],count[0], 'r-',tempe[1],count[1], 'g-',tempe[2],count[2], 'b-',tempe[3],count[3], 'o-',tempe[4],count[4], 'd-',tempe[5],count[5], 'w-',tempe[6],count[6], 'c-',
         tempe[7],count[7], 'm-',tempe[8],count[8], 'y-',tempe[9],count[9], 'k-')
a.set_xticklabels([1,2,3,4,5,6,7,8,9],rotation=45)
#a.set_xticklabels(['12/1','12/3','12/5','12/7','12/9','12/11','12/14','12/16','12/24','12/28','12/30'],rotation=45)
#for label in a.get_xticklabels():
 #       label.set_rotation(45)
#plt.legend('mean_catch')
plt.title("the site"+ str(num[i])+" temperature catch ",fontsize=20)
plt.ylabel('catch')
plt.xlabel('temperature')
plt.savefig(save_dir+"plot_site "+str(num[i])+" _catch_temperature .png")
plt.show()            