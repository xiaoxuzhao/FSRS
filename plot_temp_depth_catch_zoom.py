
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:00:48 2018
running average
@author: xiaoxu zhao
"""
from __future__ import division
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
from pandas import read_csv
from numpy import convolve
import matplotlib.pyplot as plt
from dateutil.parser import parse
import pandas as pd
####################
#HAEDCODES
input_dir='C:/Users/11307/Documents/python/paper/files/'
save_dir='C:/Users/11307/Documents/python/paper/figures/'
#input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
#save_dir='/home/zdong/xiaoxu/FSRS/figure/'
year='2006'
num=[1,2,3,4,5,6,7,8,9,10]
i=0
file='sites_good_depth.csv'
####################
def runningMean(x, N):
    y = np.zeros((len(x),))
    for ctr in range(len(x)):
         y[ctr] = np.sum(x[ctr:(ctr+N)])
    return y/N
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
time=[]
c=[]
temp=[]
for s in range(len(site)):
    if site[s]==num[i] and date[s][0:4]==year:
            c.append(s)
            time.append(parse(date[s][0:10]))
            a=((temperature[s].replace("[","")).replace(']','')).replace("'","")
            temp.append(a)
c=c[0:-19]
time=time[0:-19]
temp=temp[0:-19]
mean_count=mean_count.loc[c]
max_count=max_count.loc[c]
min_count=min_count.loc[c]
#temperature=list(temperature.loc[c])
depth=depth.loc[c]
host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
par2 = host.twinx()
offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))
par2.axis["right"].toggle(all=True)
host.set_xlabel("Date")
host.set_ylabel("Temperature",color="r")
par1.set_ylabel("Depth",color='g')
par2.set_ylabel("Catch",color='b')
for label in host.get_xticklabels():
        label.set_rotation(50)
p1, = host.plot(time, temp,'r-',label="Temperature")
p2, = par1.plot(time, depth,'g-', label="Depth")
p3, = par2.plot(time, mean_count,'b-', label="Catch")
y_av = runningMean(mean_count, 4)
par2.plot(time, y_av,"black")
plt.legend(('temperature', 'depth', 'catch','average'))
plt.title("the site "+str(num[i])+ "with catch temperature depth "+year,fontsize=20)
plt.savefig(save_dir+"plot_site( "+str(num[i])+")_catch_temp_depth "+year+".png")
plt.show()