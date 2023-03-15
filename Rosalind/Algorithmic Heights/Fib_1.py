# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 01:00:32 2021

@author: Shams
"""

def fib(n):  #still recusrive no?
    fibarray= [0,1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n <= len(fibarray):
        return fibarray[n-1]
    else:
        new_val= fib(n-1) + fib(n-2)
        fibarray.append(new_val)
        return new_val
    
def fib1(n): #non recursive
    Fib_num = [0,1]
    if n == 0:
        return 0
    if n ==1:
        return 1
    if n < 0:
        print('Error, neg input')
        return('Error, neg input') 
    if n<= len(Fib_num):
        return Fib_num[n-1]
    else:   #O(n) time 
        counter = 2
        while counter <= n:
            new_val = Fib_num[counter-1] + Fib_num[counter-2]
            Fib_num.append(new_val)
            counter += 1
    return Fib_num[n]        
            
            
        
            