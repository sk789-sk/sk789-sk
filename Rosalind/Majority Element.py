# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:38:44 2021

@author: Shams
"""

#Majority Element Problem
#Majority element using boyers voting algorithm
#We have a counter identify the number of times an element if seen, we only keep track of 1 element so O(1) auxillary space
#The first element is set to the element of interest and we increment the counter to 1.
#As we traverse throught the list we increment the counter if the read value is equal to the element and decrement otherwise
#If out counter hits 0 then the next value read becomes the new element of interest.
#The idea is that if something is truly the majority element there will be more increments then decrements.
#A pretty clear flaw is that lets say we had a list that was A,A,A,B,B,B,C. then under the current system we would end up with C being read as the majority element when there is no majority element present
#A,A,A,A,B,B,B,C would result in A =4 then A = 0 and is the currenct candidate equal so we select it is majority element correctly.
#The first case issue is still present so we have to run a second pass to see how many times C comes up and see if it is a true majority element.
#As a result 2 passes is needed of length N so linear time algo 

def majelem(array):
    counter = 0
    candidate = array[0]
    for i,val in enumerate(array): #loop through array once to get candidate
        if array[i] == candidate:
           counter +=1 
        elif array[i] != candidate:
           counter -=1
           if counter <0: #since this only occurs after rejecting from a 0 val element we would assign here and its fine
               candidate = array[i]
               counter = 1
    counter = 0 
    for x in array:  #second loop to see if candidate is good
        if x == candidate:
            counter +=1
    if -(-len(array)//2) >= counter: #ifcandidate is no good set to -1 meaning no candidate
        candidate = -1
    return candidate

def getdata(file):
    f = open(file)
    data = f.readlines()
    k,n = data[0].split()
    samplen = int(k)
    #samplemax1 = int(n)
    outarray = [0]*samplen
    for i in range(samplen):
        testarray = data[i+1].split()
        outarray[i] = majelem(testarray)
    f.close()
    return outarray    
#my input is a text file where each line is an array


majelem(['5', '1', '6', '7', '1', '1', '10', '1'])