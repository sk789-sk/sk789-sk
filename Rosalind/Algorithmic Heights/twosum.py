# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:59:01 2021

@author: Shams
"""

#2SUM
#given K arrays of length n each A1..Ak 
#return indexces where Ak[a] = -Ak[q]
#find if a numbers has the negative of if it in the array somehwere

#What if i sort the array first and then check values from each end
#Ex: array is [-5,-3,-2,-1,0,2,4,6,10] after sorting
#while -1*array[idx] > 0: so loop stops once we hit a positive number, instead of a cross
#I take the first value and compare it to the last if abs(first) is larger than the last value
#then the opposing value can not be in the array and we increment the first value by 1 
#If the first value is smaller than the opposite number may be in the array and we drop the end value by 1
#If values are equal we return the value to a list to find in original array and get all index in 1 pass
#This was we can verify if a value is in the array in n/2 steps 
#so nlogn to sort the array, then n n/2 steps to find all values that meet criteria and then n steps to get the indexes
#O(nlogn + n/2 + nk)

#WAS FROM SO LONG AGO IM JUST GOING TO REWRITE IT
from HeapSort import *

def checkexist(array): #jsut a test for now
    copy = heapsort(array[:])
    valuelist = []
    idx = 0 
    end = len(copy)-1
    while -1*copy[idx] >=0:
        if -1*copy[idx] == copy[end]:
            valuelist.append(copy[idx])
            valuelist.append(copy[end])
            idx +=1
            end -=1
            break #i think the rosalind problem only wants 1 instance, doesnt specify if its first instance or not
        elif -1*copy[idx] > copy[end]:
            idx+=1
        else:
            end -=1
    return valuelist
a = [1,2,3,-4,-3,-1]
checkexist(a)

def twosum(array): #return a list of tuples which have the 2 indexes that satify.
    vals = checkexist(array)
    if vals == []:
        return [-1]
    idxlist = [] #return values as adjacent vales in list, could return as tuple to look nicer
    i = 0
    while i < len(vals)-1:
#tuples        idxlist.append((array.index(vals[i+1])+1,array.index(vals[i])+1))
       idxlist.append(array.index(vals[i+1])+1)
       idxlist.append(array.index(vals[i])+1)  
       i+=2
    return idxlist 
       
def getdata(file):
    f = open(file)
    t = open("out.txt","w+")
    #outarray = []
    next(f) #skip the first line 
    #Lets read one line run the code then repeat until eof
    for line in f:
        a = list(map(int,line.split())) #read and format line why is this 8946 values when it is 8650 values in code what is going on 
        out = slowcheck(a)                 #check for 2sum      
        for value in out:
            t.write(str(value)+ ' ')
        t.write('\n')
    t.close()
    f.close()
    return None

#getdata('rosalind_2sum.txt')

# def getdata(file):
#     f = open(file)
#     data = f.readlines()
#     a = list(map(int,data[1].split()))
#     k = int(data[2])
#     out = ksort(a,k)
#     f.close()
#     f= open("out.txt","w+")
#     for value in out:
#         f.write(str(value)+ ' ')
#     return out        

def slowcheck(array):
    i = 0
    while i < len(array): 
        val = array[i] 
        for x in range(i+1,len(array)):
            if -1*val == array[x]:
                return [i+1,x+1] 
        i+=1       
    return [-1]
#x = [1,2,4,3,6,26,2,7,57,3,2,62,72,7,2,75,73,7,3,-26]
#slowcheck(x)



            
        
        
        