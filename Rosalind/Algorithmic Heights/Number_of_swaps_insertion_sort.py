# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:09:37 2021

@author: Shams
"""

#Overlay Graphs
#wtf it deleted it all?

def coutnerinsert(array):
    n = len(array)
    swapcount = 0
    start = 0 
    while start < n-1:
        if array[start] > array[start+1]:
            swapcount += 1
            placeholder = array[start]
            array[start] = array[start+1]
            array[start+1] = placeholder
            start = 0 #reset to start position cause lazy and dont want to write more
        else:
            start +=1
    return array, swapcount        
            
    
            