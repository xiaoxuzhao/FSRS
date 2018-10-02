# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:22:11 2018

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
i=0
year='2008'
####################
def runningMean(x, N):
    y = np.zeros((len(x),))
    for ctr in range(len(x)):
         y[ctr] = np.sum(x[ctr:(ctr+N)])
    return y/N
###################
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
for s in range(len(site)): 
    if site[s]==num[i] and date[s][0:4]==year:
            c.append(s)
            time.append(parse(date[s][0:10]))
c=c[0:-12]
time=time[0:-12]
mean_count=mean_count.loc[c]
max_count=max_count.loc[c]
min_count=min_count.loc[c]
fig = plt.figure()
a=fig.add_subplot(1,1,1)
y_av = runningMean(mean_count, 4)
plt.plot(time,mean_count, 'b-',time,max_count,'r-',time,min_count,'g-',time,y_av,'c-')
#a.set_xticklabels(['3/14','3/28','4/11','4/25','5/09','5/23'],rotation=45)
#a.set_xticklabels(['12/1','12/3','12/5','12/7','12/9','12/11','12/14','12/16','12/24','12/28','12/30'],rotation=45)
for label in a.get_xticklabels():
        label.set_rotation(30)
plt.legend(('mean catch', 'max catch', 'min catch','average'))
plt.title("the site"+ str(num[i])+" with catch "+year,fontsize=20)
plt.ylabel('catch')
plt.xlabel('date')
plt.savefig(save_dir+"plot_site(1)_catch "+year+".png")
plt.show()

