# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 09:43:52 2018
plot temp catch depth 
@author: xiaoxu zhao
"""
#[1, 16, 73, 97, 145, 216, 250, 329, 369, 418]the index of sites which
#days more than 1000 days
from pandas import read_csv
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
from dateutil import parser
import matplotlib.pyplot as plt
####################
#HAEDCODES
input_dir='/home/zdong/xiaoxu/FSRS/all_files/'
save_dir='/home/zdong/xiaoxu/FSRS/figure/'
s=0
index_mt3=[1,16,73,97,145,216,250,329,369,418]
####################
df=read_csv(input_dir+'Match_catch_good_depth.csv')
dfh=read_csv(input_dir+'fsrs_sites(1000days).csv')
index_1000=list(dfh.icol(1))
index_first=list(df.icol(1))
print index_1000
row_index=[]
for i in range(len(index_first)):
    if index_first[i]==index_mt3[s]:
            row_index.append(i)
            p=index_1000[s]
print row_index
df[row_index[0]:row_index[-1]].to_csv(input_dir+str(p)+"_site_sort_good_depth.csv", index=False)
df=read_csv(input_dir+str(p)+"_site_sort_good_depth.csv")
df = df.sort("Date")
index_sites=df["index_sites"]
date=df["Date"]
Mean_temp=df["Mean_temp"]
depth=df["Depth"]
catch=df["Catch"]
print catch
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

p1, = host.plot(Date, Mean_temp, 'r.',label="Temperature")
p2, = par1.plot(Date, depth,'g.', label="Depth")
p3, = par2.plot(Date, catch,'b.', label="Catch")
#host.xticks(pd.date_range('2018-01-01','2009-05-1'),rotation=90)
host.set_xticks(['2004','2006','2008','2010','2012','2014'])
#'2004','2005','2006','2007','2008','2009','2010',
host.set_title("the site"+index_mt3[s]+"Temperature ,Depth and catch")

host.legend(loc=9,fontsize=6)

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())

plt.savefig(save_dir+index_mt3[s]+"_site_temperature_depth_catch.png")
plt.show()
