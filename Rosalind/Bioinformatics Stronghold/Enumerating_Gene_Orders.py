# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 15:02:25 2021

@author: Shams
"""

#permute list

import math as m

def listgen(n):
    x = m.factorial(n)
    big_list = []
    sublist = [0] * n
    for y in range(0,x):
        big_list.append(sublist)
    return big_list    

def tree_gen(n):
    array = []
    for val in range(0,n):
        array.append(val)
    
#kinda weird way of doing it next?
#We build the lists up starting from 2 elements, by inserting the values in between lists
#so in the case of 1,2,3,4 we have 2 lists then 6 lists then 24 lists

def buildperm(n): #We build the list of permutation by introducing 1 number at a time
    x = [[1]]     #first find all permutations of 1, then add 2 and find all combos of 1,2, then 1,2,3 until n 
    if n == 1:    #since we have a list of all permutations previously we just add the new number at all possible indexes to list of new perms
        return [1]
    st = list(range(2,n+1))
    for new_n in st:
        y = []
        for subl in x:
            for val in range(0,len(subl)+1):
                t = subl[:]
                t.insert(val,new_n)
                y.append(t)
        x = y[:]
    return x

#t=buildperm(3)
#n=buildperm(4)

def getdata(file):
    f = open(file)
    n = int(f.readline())
    f.close()
    x = buildperm(n)
    t = open('out.txt', 'w+')
    t.write(str(len(x))+'\n')
    for lst in x:
        for val in lst:
            t.write(str(val)+' ')
        t.write('\n')
    t.close()
    return x


    
    