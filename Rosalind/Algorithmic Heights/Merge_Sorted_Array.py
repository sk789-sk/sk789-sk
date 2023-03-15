# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:42:40 2021

@author: Shams
"""

#Merge two sorted arrays:
#Given Sorted array A[1:n] and Sorted array B[1:m] return the sorted array C which is the merged of A,B C[1:m+n]
#Initial Logic: We compared the first 2 values of A and B. We then see which is one is smaller and then add that value to a new array
#We then remove that value from the approriate array(A or B) and compared again:
#Ex: A= [ 2 4 10 18] and B= [-5 11 12]
#C1 : -5 vs 2 so C[-5] , A[2 4 10 18] , B[11 12]
#C2 : 2 vs 11 so C[-5 2], A[4 10 18] , B = [11 12]
#C3 : 4 vs 11 so C[-5 2 4], A[10 18], B = [11 12] 
#C4-(m+n) : same idea
#If any array becomes empty then we just append the other array to the new array
#We can solve this recursively since we just do a comparison of A[1],B[1]

def mergesortedarray(array1,array2,outarray):
    #Could probably do this better with counters for length instead
    if array1 == []: #if first array is empty then add all valuesin array 2 to out
        for idx,val in enumerate(array2):
            outarray.append(array2[idx])
        return outarray
    if array2 == []: #if second array is empty then add all values in array 1 to out
        for idx,val in enumerate(array1):
            outarray.append(array1[idx])
        return outarray    
    #pick which value to add to array
    if array1[0] > array2[0]:
        outarray.append(array2[0])
        return mergesortedarray(array1,array2[1:],outarray)
    else:
        outarray.append(array1[0])
        return mergesortedarray(array1[1:],array2,outarray)
        
def getdata(file):
    f = open(file)
    data = f.readlines()
    a = list(map(int,data[1].split()))
    b = list(map(int,data[3].split()))
    #c = [] commented out for iterative
    #out = mergesortedarray(a,b,c) #commented out for iterative
    out = nonrecursivemerge(a,b)
    f.close()
    f= open("out.txt","w+")
    for value in out:
        f.write(str(value)+ ' ')
    return out  
    
#Ok so this function works but 20k values causes recursion limit and could cause a stack overflow
#Lets do it without recursion then:

def nonrecursivemerge(a,b): #iterative way to merge 2 sorted arrays
    c = [] 
    al = len(a)
    bl = len(b)
    c1,c2 = 0,0
    while c1 < al and c2 < bl: #could use ques to pop values, and not just check if either list is empty
        if a[c1] < b[c2]:
            c.append(a[c1])
            c1 += 1
        else: #a[c1] >= b[c2]:
            c.append(b[c2])
            c2 += 1
    if c1 == al:
        for val in (b[c2:]):
            c.append(val)
    else:
        for val in (a[c1:]):
            c.append(val)
    return c 
    
#so i lost a file "pointer" since i had an exception before it closed, from now on use the with method so that even if the program stops due to 
#some reason the file still closes.     
    
d = [2,4,18,19]
e = [-5,11,12]
a = [1,3,5,7,9,11]
b = [2,4,6,8,10,12]
#nonrecursivemerge(d,e)
nonrecursivemerge(a,b)
