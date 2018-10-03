# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:03:23 2018
process raw file ,delete catch empty lines and temperature =-99.00 398538---371847
@author: xiaoxuzhao
"""
from pandas import read_csv
import numpy as np
import re
################
input_dir='/home/zdong/xiaoxu/paper/file/'
save_dir='/home/zdong/xiaoxu/paper/figure/'
###############
df=read_csv(input_dir+'355c0671cde98eb5386b570c663fc7327e374d77.csv')
info=df["dynamicProperties"]   
count=df["individualCount"]
temp=[str(i)[36:62] for i in info]   #extract  Bottom temperature=1.01C;,SampleSize=Trap deployed for 8 days; Bottom temperature=1.01C;
a=[re.findall(r"[-+]?\d*\.\d+|\d+", i) for i in temp]
for i in range(len(count)) :#len(count)
    if np.isnan(count[i]) or  a[i]==["-99.00"]:
        print i
        df.drop(i, inplace=True)
print df
df.to_csv(input_dir+'new_file.csv')
