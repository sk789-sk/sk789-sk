# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 15:34:06 2021

@author: Shams
"""

#MergeSort
#We already have an algorithm to merge 2 sorted arrays from earlier so were just gonna copy paste that in here

def nonrecursivemerge(a,b): #iterative way to merge 2 sorted arrays
    c = [] 
    al = len(a)
    bl = len(b)
    c1,c2 = 0,0
    while c1 < al and c2 < bl: #could pop values, and not just check if either list is empty
        if a[c1] < b[c2]:
            c.append(a[c1])
            c1 += 1
        else: #a[c1] >= b[c2]:
            c.append(b[c2])
            c2 += 1
    if c1 == al:
        c+= b[c2:]
    else:
        c+= a[c1:]
#        for val in (a[c1:]):
#           c.append(val)
    return c #if i try to count inversion like this ill have tuples and need to adjust for that
#note this is not in place
    
def mergesort(array):
    if len(array) ==1:
        return array
    array1 = array[:len(array)//2]
    array2 = array[(len(array)//2):]
    a1 = mergesort(array1)
    a2 = mergesort(array2)
    return nonrecursivemerge(a1,a2)
    
def getdata(file):
    f = open(file)
    data = f.readlines()
    a = list(map(int,data[1].split()))
    out = mergesort(a)
    f.close()
    f= open("out.txt","w+")
    for value in out:
        f.write(str(value)+ ' ')
    f.close()    
    return out 

test = [4,7,8,9,3,2,9,4]
mergesort(test)