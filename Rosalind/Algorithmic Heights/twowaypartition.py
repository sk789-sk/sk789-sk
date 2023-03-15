# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:30:56 2021

@author: Shams
"""

#2 way partition
#Basically I have an array, and I take the first value in the array n 
#permute the array so that all value less then the n are on the left side of n, and all values greater are on the right
#the values do not need to be in order

def twowaypartition(array):
    #Take the input value and compare it to the next, if it is smaller then move to front If it is larger we can just move it the back of the array. We do n-1 comparisons
    #better if i keep track on new index and check when index crosses
    n = len(array)
    val = array[0]
    count = 0
    while count < len(array):
        if array[n-1] < val:
            array.insert(0,array.pop(n-1))
            count +=1              
        else:
            n -=1
            count +=1
    return array
            
def getdata(file):
    f = open(file)
    data = f.readlines()
    a = list(map(int,data[1].split()))
    out = twowaypartition(a)
    f.close()
    f= open("out.txt","w+")
    for value in out:
        f.write(str(value)+ ' ')
    return out 