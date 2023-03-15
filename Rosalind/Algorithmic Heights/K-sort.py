# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 19:23:43 2021

@author: Shams
"""

#return the k smallest elements in the list

#We could do heapsort and return the first k elements so that would be nlogn
#Aternatively we could build a min heap which is O(n) time and then we do k steps in heapsort(percolate down) each taking log n time
#this would be klogn time and k<n so this is better
#modify existing code to make it a min heap instead
#Not sure if it wants it to be returned in order or not.

def array2heap(array): #turn array into heap O(n) if i did it right
    idx = (len(array)//2) -1 #index of first parent node w/ child
    while idx >=0:
        array = percolatedown(array,idx)
        idx -=1
    return array

def percolatedown(array,idx): #push a value down in the heap
    while idx <= (len(array)//2) -1: #not a leaf criteria
        lchild = (2*idx)+1
        rchild = (2*idx)+2
        if rchild == len(array): #Edge where the first parent only has a left child
            if array[idx] > array[lchild]:
                swapelement(array,idx,lchild)
                idx = lchild
            else:
                return array
        else:
            #Check which child is smaller
            out = rchild if (array[rchild] <= array[lchild]) else lchild
            if array[idx] > array[out]: #compare parent with smaller child and swap is parent > child
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

def ksort(array,k):
    array = array2heap(array) #turn array into heap
    end = len(array)-1 #get the end of the heap
    count = k
    while k > 0: #loop to sort the heap and reduce heap size by 1
        swapelement(array,0,end) #swap
        k,end = k-1,end-1 #reduce heap size by 1
        array[0:end+1] = percolatedown(array[0:end+1],0) #update array to match new heap
    return array[-count:][::-1]

def getdata(file):
    f = open(file)
    data = f.readlines()
    a = list(map(int,data[1].split()))
    k = int(data[2])
    out = ksort(a,k)
    f.close()
    f= open("out.txt","w+")
    for value in out:
        f.write(str(value)+ ' ')
    return out

getdata('test.txt')
