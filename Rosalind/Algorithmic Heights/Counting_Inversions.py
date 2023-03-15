# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:06:04 2021

@author: Shams
"""

#Counting Inversions
#An inversion in an array is when there is a pair on indexes (i,j) for indexes 1 <= i <=j, n
#Where A[i] > A[j]. Basically this means i and j are out of order. If a list is sorted then there are 0 inversions.. If a list is in reverse order then we are max inversions.

#Idea is we could check each value against the current index and iterate multiple times through the array
#Frist time would be n-1 comparisons, then n-2, n-3 until we hit 1. Ithink this is n^2 time then 




def inversioncounter(array): #slow brute way
    counter,idx = 0,0
    #n = len(array)
    while idx < len(array):
        for val in array[idx:]:
            if array[idx] > val:
                counter +=1 
        idx +=1
    return counter

def fastinv(array):
    #Just make an adjustment to the mergesort to count inversions
    #Whenever we make are combining arrays in mergesort we have A[] and B[]. which are both sorted
    #With how mergesort works array A will have values to the left of array B. therefore when merging arrays
    #A and B anytime we add an element from B to the new array instead of A that means all the elements in remaining in A are larger than the value in B.
    #so the number of inversions at that join are all the elements left in array A. We keep a tally of this and return this value
    #seems kinda silly tho to see how many inversions there are we have to sort the array
    #should try to find a way to do this without sorting the array fully
    out = mergesort(array)
    return out[1]


def nonrecursivemerge(a,b): #combine 2 arrays and keeps track of inv. Ugly but it works 
    c = [] 
    inv_t,inv_t2 = 0,0
    if isinstance(a,tuple): inv_t = a[1];a = a[0]
    if isinstance(b,tuple): inv_t2 = b[1];b = b[0]
    al = len(a)
    bl = len(b)
    inv_c = inv_t+inv_t2
    c1,c2 = 0,0
    while c1 < al and c2 < bl: 
        if a[c1] <= b[c2]: #make <= so ties dont add extra inversions
            c.append(a[c1])
            c1 += 1
        else: #a[c1] >= b[c2]:
            c.append(b[c2])
            c2 += 1
            inv_c += len(a[c1:])
    if c1 == al:
        c+= b[c2:]
    else:
        c+= a[c1:]
    return c, inv_c 

    
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
    out = fastinv(a)
    f.close()
    f= open("out.txt","w+")
    f.write(str(out)+ ' ')
    f.close()    
    return out 
