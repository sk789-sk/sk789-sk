# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:29:28 2021

@author: Shams
"""

def mortal_pop(n,k,t,life): #n=number of months, k=#of litter,t=time for maturity life=life span in months
    bp_pop_month = [0]* (n) #initale array of values
    np_pop_month = [0]* (n) #initialize array of values
    bp_pop_month[0] = 0       #inital condition
    np_pop_month[0] = 1       #initial condition
    i = 1 #counter
    while i <(n): #month 1 = index 0  
        np_pop_month[i] = k*bp_pop_month[i-1]    #new bp is just the litter from all breeding pairs from last
        if i<life: #array length until we reach life cycle would be out of range to seperate since no deaths as well
            bp_pop_month[i] = bp_pop_month[i-1]+np_pop_month[i-t] #breed pair calc
        else:
            bp_pop_month[i] = bp_pop_month[i-1]+np_pop_month[i-t]-np_pop_month[i-life] #make sure to consiter when the intial state is out of range
        i+=1
    return bp_pop_month,np_pop_month,np_pop_month[i-1]+bp_pop_month[i-1] #array for bp,np,total