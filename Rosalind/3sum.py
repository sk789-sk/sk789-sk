# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:10:30 2021

@author: Shams
"""

#3sum 3 integers that sum to 0
#I could check first value remove it and do 2sum with the remaining values 
#Each time we would be shortening the array by 1 
#so we end up doing n 2sum problems, but each 2sum is getting faster each time
#So we could do it with the heap method, but that method was right, but rosalind wouldnt accept it, maybe it has to be the first index? 
#if thats the case we need to build a new heap every single time so the total running time is n*nlogn*k. Hash would be n^2 + time to build hash O(n)
#in that case we can just do the slow method agian and hope its within time limit
from HeapSort import * 

# WAS FROM SO LONG AGO JUST REDO FROM SCRATCH
# =============================================================================
# # def threesum(array): Brute Method
# #     i = 0
# #     while i < len(array): #n
# #         goalval = array[i]
# #         j = i+1
# #         while j < len(array): #n/2
# #             subgoal = array[j]
# #             for x in range(j+1,len(array)): #n/2
# #                 if subgoal + array[x] == -goalval:
# #                     return[i,j,x]
# #             j+=1
# #         i+=1
# #     return[-1]
# 
# #ok that is way to slow so lets do it with a hash or sorted array:
# 
# def checkexist(array): #checks for 3sum criteria and returns values for it runs fairly quick
#     copy = heapsort(array[:])
#     #copy = sortedarray
#     valuelist = []
#     i = 0 
#     while i < len(copy): #O(n)
#         idx = i+1
#         goal = -copy[i]
#         end = len(copy)-1
#         while end > idx: #O(n/2)
#             if copy[idx] + copy[end] == goal:
#                 valuelist.append(copy[i])
#                 valuelist.append(copy[idx])
#                 valuelist.append(copy[end])
#                 idx +=1
#                 end -=1
#                 return valuelist #i think the rosalind problem only wants 1 instance, doesnt specify if its first instance or not
#             elif copy[idx] + copy[end] < goal:
#                 idx+=1
#             else:
#                 end -=1
#         
#         i +=1
#     return [-1]
# Returns results, but since it only sort once, and use that array not necessarily the first value from the starting unsorted array
# =============================================================================

#I think rosalind just wants the first solution available so lets just do 2 sum with the first value as the goal in the list 
#So just take out the first value in the array, do 2 sum with the sorted array and run with it

#so far O(n^2) to find the values for each array. Now I need to find  corresponding indexes

# def find3sums(sortedarray,goal): #jsut a test for now
#     i = 0  
#     end = len(sortedarray)-1
#     valuelist = []
#     while end > i: 
#         if sortedarray[i] + sortedarray[end] == -goal:
#             valuelist.append(sortedarray[i])
#             valuelist.append(sortedarray[goal])
#             valuelist.append(sortedarray[end])
#             return valuelist #i think the rosalind problem only wants 1 instance, doesnt specify if its first instance or not
#         elif sortedarray[i] + sortedarray[end] < goal:
#             i+=1
#         else:
#             end -=1
#     return [-1]
   

# def threesum(array):
#     copy = heapsort(array[:]) #O(n)
#     out = []
#     for x in array: ##O(n)
#         t = find3sums(copy,x) #O(n) 1 pass through the array
#         if len(t) == 3:
#             for val in t:
#                 out.append(array.index(t))    
#             return out
#     return [-1]    
        
#logic is to just do 2 sum with the first element removed each time

#These methods work, but since resort each time its slow. 
def threesum(array):
    i= 0
    while i < len(array):
        goal = array[i]
        x = twosum(array[i+1:],-1*goal)
        if x != -1:
            j = array.index(x[0]) #this will break if the values are equal since it just returns first idx twice
            k = array.index(x[1])
            idxtest = {i,j,k} #write this in after 
            return (i+1,j+1,k+1) #rosalind idx starts at1
        i +=1 #try again with the next idx
    return -1
        
def twosum(array,goal):
    c_array = heapsort(array[:])
    lc = 0 
    rc = len(c_array)-1
    while lc < rc:
        if (c_array[lc] + c_array[rc]) == goal:
            return c_array[lc],c_array[rc]
        elif c_array[lc] + c_array[rc] > goal: 
            rc -=1
        else:
            lc +=1
    return -1 

def getdata(file):
    with open(file) as f, open('out.txt', 'w+') as t:
        data = f.readlines()
        for val in data[1:]:
            a = list(map(int,val.split()))
            out = threesumhash(a)
            for val in out:
                t.write(str(val)+' ')
            t.write('\n')
    return

#Ok the heapsort method is still to slow so we have to use a hash 

def threesumhash(array): #Cant i just do in with an array guessing its O(n) with arrays
    x = dict()
    for val in array:  #Create the hash so on^3 slower then n*nlogn no?
        x[val] = None  
    for idx1,i in enumerate(array): #this way we get the first value should be o(n^2)
        for idx2,val in enumerate(array[idx1+1:]):
            goal = -i-val 
            if goal in x: #check to see if we have double count 
                out = array.index(goal) #would break in case of array = [2,0,0,-4,2] since .index returns first instance and 2,4,2 is the satisfying triplet, would return idx 0 twice
                if out == idx1 or (idx1+idx2+1):
                    x = idx1 if out == idx1 else idx1+idx2+1
                    for idx3,val2 in enumerate((array[x+1:])):
                        if val2 == goal:
                            return (idx1+1,idx1+idx2+1+1,idx3+x+1+1) #the extra +1's for rosalind idx 1 start
                return (idx1+1,idx1+1+idx2+1,out+1) #(i,val,goal)
    return [-1]

#The first submission I did should have worked. I reran it with the hash table version and the output matched the output i did the first time
#It had 1 answer in incorrect order where the largest value was listed second, but the rest did not not sure why. 