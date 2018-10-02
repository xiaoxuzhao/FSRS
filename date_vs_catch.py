# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:24:59 2018

@author: xiaoxu zhao
"""
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
from dateutil.parser import parse
#####################
#HARDCODES
input_dir='/home/zdong/xiaoxu/paper/file/'
save_dir='/home/zdong/xiaoxu/paper/figure/'
file='sites_good_depth.csv'
num=[1,2,3,4,5,6,7,8,9,10]
i=0
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
for s in range(len(site)): 
    if site[s]==num[i]:
            c.append(s)
            time.append(parse(date[s][0:10]))
#date=date.loc[c]
mean_count=mean_count.loc[c]
max_count=max_count.loc[c]
min_count=min_count.loc[c]
fig = plt.figure()
a=fig.add_subplot(1,1,1)
plt.plot(time,mean_count, 'b+',time,max_count,'r+',time,min_count,'g+')
a.set_xticks(['2005','2007','2009','2011','2013','2015'])

plt.legend(('mean catch', 'max catch', 'min catch'))
plt.title("the site 1 with catch",fontsize=20)
plt.ylabel('catch')
plt.savefig(save_dir+"plot_site(1)_catch.png")
plt.show()
