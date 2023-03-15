# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:42:46 2021

@author: Shams
"""
#Quicksort
# =============================================================================
# 
# Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
# 
# Return: A sorted array A[1..n].
# =============================================================================

from random import randint
#lets do this without extra memory so adjust functions as needed

def partition(array): 
    if len(array) < 1:
        return 0
    pivot = randint(0,max(1,len(array)-1))
    #pv = array[pivot]
    swap(array,pivot,-1)  #moves the pivot to the end
    lc = 0  #idx of left counter
    rc = max(1,len(array)-2) #idx of right counter
    while lc < rc: #wont this break if all the values are the same?
        while array[lc] < array[-1]:
            lc +=1
        while array[rc] > array[-1]:
            rc -=1
        if lc < rc:
            swap(array,lc,rc)
    swap(array,lc,-1)
    return lc

def swap(array,first,second): #first and second are idx
    array[first],array[second] = array[second], array[first]    

def qs(array):
    pivot_point = partition(array)
    if len(array[:pivot_point]) <=1:
        qs(array[:pivot_point])
    if len(array[pivot_point+1:]) <=1:
        qs(array[pivot_point:])
    

#test = [556,642,942,736,543,488,75,527]
#qs(test)

test2 =[1, 2, 4, 5, 13, 8, 11, 20, 21, 36, 5]
qs(test2)

#t2 = [1, 8, 3, 3, 5, 5, 7, 7, 2, 2, 4, 4, 8, 9, 9, 1]
#partition(t2)