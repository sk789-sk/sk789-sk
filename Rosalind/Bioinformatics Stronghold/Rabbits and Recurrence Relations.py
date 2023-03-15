# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:07:40 2021

@author: Shams
"""

#Find the population of rabbits at N months given the following critera
#1) Rabbits are immortal
#2) After each month each newborn rabbit pair progresses to a breeding pair
#3) Every breeding pair produces k newborn rabbit pair(male+female) each month
#4) At month 1 we start with 1 newborn rabbit pair 

def pop(n,k):  #n = number of months and k = number of litter given by 1 breeding pair
    bp = 0     #bp = breeding pair initially start with 0
    np = 1     #np = newborn pair initially start with 1
    while n > 1:   #month counter 
        #at each n, every newpair progresses to breeding pair
        #every breeding pair results in k newpairs so k x bp
        prev_bp = bp    #keep old val for calc
        prev_np = np    #keep olf val for calc
        np = prev_bp*k  #k litters for each breeding pair
        bp = prev_bp + prev_np #all previous breeding pair continues and newborns become breeders  
        n -=1     #counter
    return bp+np   #total population  

#this feels like a better solution than recursion since we just keep the values and adjust them so only n loops with constant work per loop so O(n)
    
#pop(5,3)