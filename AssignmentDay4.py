# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:56:22 2020

@author: Personal
"""
start = 1042000
end = 702648265
temp = ""
temp1 = 0
while(start<end):
    temp = str(start)
    temp1 = 0
    for i in range (len(temp)):
        temp1 = temp1 + pow(int(temp[i]),len(temp))
    #print(temp1)
    start = int(start)
    #print(start , "  " , temp1)
    if temp1 == start:
        print ("The First Armstrong number betwen 1042000 and 702648265 is" , start)
        break
    else:
        start = start+1
    
#The First Armstrong number betwen 1042000 and 702648265 is 1741725 #    