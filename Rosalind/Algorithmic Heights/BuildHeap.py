# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:10:21 2021

@author: Shams
"""

#Build a max heap from an array
#Properties to take advantage of:
#1) A nodes children is 2j,2j+1
#2) A nodes parent is floor(j//2)
#)for index zero parent is (j-1//2), child is 2j+1,2j+2 

#So For each node first we check its child and compare.
#Then we check its parent and compare if a swap is needed
#We would need to continously check parents

#Alternatively we could just build a max heap from the array as inserts 1 by 1.
#Lets try both way 

def buildmaxheap(array): #Building the heap with just inserts nlogn
    heaparray = []
    for n in array:
        heaparray = insertmaxheap(heaparray,n) #just building the heap with inserts
    return heaparray

def insertmaxheap(array,n): #insert heap logn
    if array == []:
        array.append(n)
        return array
    array.append(n)
    ins_idx = len(array)-1 
    #parent_idx = ((ins_idx-1)//2) 
    while ins_idx >0: #means not at root 
        if array[ins_idx] >= array[(ins_idx-1)//2]:
            swapelement(array,(ins_idx-1)//2,ins_idx)
            ins_idx = (ins_idx-1)//2
        else: #if no need for swap, then we wouldnt swap anyway so just stop
            break
    return array

def array2heap(array): #turn array into heap O(n) if i did it right
    idx = (len(array)//2) -1 #index of first parent node w/ child
    while idx >=0:
        array = percolatedown(array,idx)
        idx -=1
    return array

def percolatedown(array,idx): #push a value down in the heap
    while idx <= (len(array)//2) -1:
        lchild = (2*idx)+1
        rchild = (2*idx)+2
        if rchild == len(array): #Edge where the first parent only has a left child
            if array[idx] < array[lchild]:
                swapelement(array,idx,lchild)
                idx = lchild
            else:
                return array
        else:
            #Check which child is bigger
            out = rchild if (array[rchild] >= array[lchild]) else lchild
            if array[idx] < array[out]: #compare parent with bigger child
                swapelement(array,idx,out)
                idx = out
            else:
                return array
    return array        

            
def swapelement(array,x,y):
    array[x],array[y]= array[y],array[x]
    return array

def heapsort(array):
    array = array2heap(array) #turn array into heap
    count = len(array)-1 #get the end of the heap
    while count > 0: #loop to sort the heap and reduce heap size by 1
        swapelement(array,0,count) #swap
        count -=1 #reduce heap size by 1
        array[0:count+1] = percolatedown(array[0:count+1],0) #update array to match new heap
    return array

def getdata(file):
    f = open(file)
    data = f.readlines()
    a = list(map(int,data[1].split()))
    out = heapsort(a)
    f.close()
    f= open("out.txt","w+")
    for value in out:
        f.write(str(value)+ ' ')
    f.close()    
    return out 


#check code i found to see where issues were happening.Helped me realize i mistyped a parent calculation 
# Python3 program to check whether a
# given array represents a max-heap or not
 
# Returns true if arr[i..n-1]
# represents a max-heap

def isHeap(arr, n):
     
    # Start from root and go till
    # the last internal node
    for i in range(int((n - 2) / 2) + 1):
         
        # If left child is greater,
        # return false
        if arr[2 * i + 1] < arr[i]:
                return False,arr[i],i,'left'
 
        # If right child is greater,
        # return false
        if (2 * i + 2 < n and
            arr[2 * i + 2] < arr[i]):
                return False,arr[i],i,'right'
    return True
 
