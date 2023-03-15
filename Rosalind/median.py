# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:03:15 2021

@author: Shams
"""

# =============================================================================
# The task is to implement a linear time randomized algorithm for the selection problem.
# 
# Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive number k≤n.
# 
# Return: The k-th smallest element of A.
# =============================================================================

#We we have an array, we can pick a random value in the array and partition the array at that point into 3 groups
#Values smaller than it, values larger than it, and values equal to it
#This way were kinda sorting but we dont do all the work for sorting
#Now if we know we want the kth number in the array and we know how many values are in the smaller, equal to , and larger arrays we can see which array the kth value will be in 
#From that we can then choose to do this same thing with the appropriate subarray and adjust the K value as needed.
#Ex: [ 1 3 4 6 2 14 3 5 5 6 13 8 5 10 9] we want the 6th smallest number
#Random pivot is 8 then:
    #Sub_L = [1 3 4 6 2 3 5 5 6 5], c = 10
    #Sub_G = [14 13 10 9], c = 4
    #Sub_E = [8] = 1

#Now we see that for sub_L there are 10 elements and since we want the 8th smallest element it should be in this sub
#Lets say we wanted the 13th smallest element, then it would have to be in the larger array. For this we can then take the value of wanted(13) and subtract the length of the L and equal array. which would mean we would want the 2nd smallest element in the larger array
#We could do this repeatedly until we guessed the pivot correctly.

def selection(array,k):
    #our random array value will just be the middle number in the array each time
    pivot = array[len(array)//2]
    ec, c = 0,0 #number of elements in the smaller array
    #Would be much better to just to the sorting in the same array each timedi
    l = []
    g = []
    e = []
    
    for val in array:
        if val < pivot:
            l.append(val)
            c +=1 
        elif val > pivot:
            g.append(val)
        else:
            e.append(val)
            ec +=1 
    if k in range(c+1,c+ec+1): #just 1 since we just need 1 equal to be good
        return e[0] 
    elif k < c+1:
        return selection(l,k)
    return selection(g,k-c-ec)

test = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]

    
    
def getdata(file):
    with open(file) as file:
        f = file.readlines()
    start_array = int(f[0])*[0]
    out = list(map(int,f[1].split()))
    for idx,val in enumerate(out):
        start_array[idx] = val
    return selection(start_array,int(f[2]))