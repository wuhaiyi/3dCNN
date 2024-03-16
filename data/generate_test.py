#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: haiyi1
norm data based on:
    DEPTH 10525.66 9010.0
    PERMX 18325.014 0.000796
    PERMY 18325.014 0.000796
    PERMZ 183.25012 8e-06
    PORO 0.654276 0.009445
    PORV 982329.5 1383.1694
    SATNUM 1.0 1.0
    TRANX 1510.4866 0.0
    TRANY 1581.2839 0.0
    TRANZ 1328.9543 0.0
    WOPR 31796.140625 0.8107147216796875
    BHP 3565.692138671875 14.50377368927002
"""

import numpy as np
import os
import matplotlib.pyplot as plt

# Load dataset
path = '/Users/haiyi1/Documents/windows/UT/Fdoc/myself/2023/industry/MLE/OriGen/origen_interview_data/valid/'
input3Ds= {'DEPTH', 'PERMX', 'PERMY', 'PERMZ', 'PORO', 'PORV', 'SATNUM',
           'TRANX', 'TRANY', 'TRANZ'}
max_val = np.array([10525.66, 18325.014, 18325.014, 183.25012, 0.654276, 982329.5, 1.0, 1510.4866, 1581.2839, 1328.9543])
min_val = np.array([9010.0, 0.000796, 0.000796, 8e-06, 0.009445, 1383.1694, 1.0, 0.0, 0.0, 0.0])
input1D = 'BHP'
output1D = 'WOPR'
max_BHP = 3565.692138671875
min_BHP = 14.50377368927002
max_WOPR = 31796.140625
min_WOPR = 0.8107147216796875
dim_3d = 15*24*25
dim_1d = 300

all_3Ds = []
for index, name in enumerate(sorted(input3Ds)):
    inp_path = path + name +'/'
    group = []
    for data in sorted(os.listdir(inp_path)):
        data_path = inp_path + data
        #print(data_path)
        inp_data = np.load(data_path).reshape(15,25,24)
        group.append(inp_data)
    max_g = max_val[index]
    min_g = min_val[index]
    print(name, max_g, min_g)  
    if min_g == max_g:
        norm_group = group
    else:
        norm_group = (group-min_g)/(max_g - min_g)
    all_3Ds.append(norm_group)
    
path_out = path + output1D + '/'
path_1D= path + input1D +'/'

array_3Ds = np.array(all_3Ds)

WOPR = []
for data in sorted(os.listdir(path_out)):
    data_path = path_out + data
    #print(data_path)
    out_data = np.load(data_path) # 7 cols for 7 wells
    WOPR.append(out_data)

array_WOPR = np.array(WOPR)
array_WOPR = (array_WOPR - min_WOPR)/(max_WOPR - min_WOPR)
print(output1D, max_WOPR, min_WOPR)

BHP = []
for data in sorted(os.listdir(path_1D)):
    data_path = path_1D + data
    #print(data_path)
    data_1D = np.load(data_path)
    BHP.append(data_1D)

array_BHP = np.array(BHP)
array_BHP = (array_BHP - min_BHP)/(max_BHP - min_BHP)
print(input1D, max_BHP, min_BHP)

# plot and check
# plt.plot (array_BHP[10,:,0], 'b-')
# plt.plot (array_WOPR[10,:,0], 'k-')
#Trany = array_3Ds[8].reshape(450,9000)
#plt.plot (Trany[1:20,:], 'k-')

plt.show()

np.savez_compressed('valid_well1', Depth = array_3Ds[0], Permx = array_3Ds[1], Permy = array_3Ds[2], 
                    Permz = array_3Ds[3], Poro = array_3Ds[4], Porv = array_3Ds[5], Satnum = array_3Ds[6], 
                    Tranx = array_3Ds[7], Trany = array_3Ds[8], Tranz = array_3Ds[9],
                    inp1D = array_BHP[:,:,0],out1D = array_WOPR[:,:,0])

np.savez_compressed('valid_well2', Depth = array_3Ds[0], Permx = array_3Ds[1], Permy = array_3Ds[2], 
                    Permz = array_3Ds[3], Poro = array_3Ds[4], Porv = array_3Ds[5], Satnum = array_3Ds[6], 
                    Tranx = array_3Ds[7], Trany = array_3Ds[8], Tranz = array_3Ds[9],
                    inp1D = array_BHP[:,:,1],out1D = array_WOPR[:,:,1])

np.savez_compressed('valid_well3', Depth = array_3Ds[0], Permx = array_3Ds[1], Permy = array_3Ds[2], 
                    Permz = array_3Ds[3], Poro = array_3Ds[4], Porv = array_3Ds[5], Satnum = array_3Ds[6], 
                    Tranx = array_3Ds[7], Trany = array_3Ds[8], Tranz = array_3Ds[9],
                    inp1D = array_BHP[:,:,2],out1D = array_WOPR[:,:,2])

np.savez_compressed('valid_well4', Depth = array_3Ds[0], Permx = array_3Ds[1], Permy = array_3Ds[2], 
                    Permz = array_3Ds[3], Poro = array_3Ds[4], Porv = array_3Ds[5], Satnum = array_3Ds[6], 
                    Tranx = array_3Ds[7], Trany = array_3Ds[8], Tranz = array_3Ds[9],
                    inp1D = array_BHP[:,:,3],out1D = array_WOPR[:,:,3])

np.savez_compressed('valid_well5', Depth = array_3Ds[0], Permx = array_3Ds[1], Permy = array_3Ds[2], 
                    Permz = array_3Ds[3], Poro = array_3Ds[4], Porv = array_3Ds[5], Satnum = array_3Ds[6], 
                    Tranx = array_3Ds[7], Trany = array_3Ds[8], Tranz = array_3Ds[9],
                    inp1D = array_BHP[:,:,4],out1D = array_WOPR[:,:,4])

np.savez_compressed('valid_well6', Depth = array_3Ds[0], Permx = array_3Ds[1], Permy = array_3Ds[2], 
                    Permz = array_3Ds[3], Poro = array_3Ds[4], Porv = array_3Ds[5], Satnum = array_3Ds[6], 
                    Tranx = array_3Ds[7], Trany = array_3Ds[8], Tranz = array_3Ds[9],
                    inp1D = array_BHP[:,:,5],out1D = array_WOPR[:,:,5])

np.savez_compressed('valid_well7', Depth = array_3Ds[0], Permx = array_3Ds[1], Permy = array_3Ds[2], 
                    Permz = array_3Ds[3], Poro = array_3Ds[4], Porv = array_3Ds[5], Satnum = array_3Ds[6], 
                    Tranx = array_3Ds[7], Trany = array_3Ds[8], Tranz = array_3Ds[9],
                    inp1D = array_BHP[:,:,6],out1D = array_WOPR[:,:,6])