# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:07:59 2021

@author: Shams
"""

#Enumerating Oriented Gene Orderings

#total number of (permutations is # of combos * 2^n)
#view it as for every permutation we generate a truth table where 1 = positive and 0 = negative.

def buildperm(n): #We build the list of permutation by introducing 1 number at a time
    x = [[1]]     #first find all permutations of 1, then add 2 and find all combos of 1,2, then 1,2,3 until n 
    if n == 1:    #since we have a list of all permutations previously we just add the new number at all possible indexes to list of new perms
        return [1]
    st = list(range(2,n+1))
    for new_n in st:
        y = []
        for subl in x:
            for val in range(0,len(subl)+1):
                t = subl[:]
                t.insert(val,new_n)
                y.append(t)
        x = y[:]
    return x

#Same perm code from previous problem

def masks(n):
    #make 2^n masks to just multiply through for each combination
    #multiply lists wont work like it would in matlab, should use numpy arrays would be bette then looping through lists and multiplying i thnk
    init = [1]*n
    masks = [init] * (2**n)
       
        
 #   [a*b for a,b in zip(masks[0],x[0])] #elementwise mult
    
    
def TTable(permlist):
    out_list = []
    for perm in permlist: #for one of the permunations we just run through it like were generating a truth table
        for val in perm:
           #TODO 
           return 1
            
# =============================================================================
# [(0,1),(1,4),(2,6),(3,4),(4,1),(5,0)]            
# [1 1 1 1]
# [-1 1 1 1]
# [1 -1 1 1]
# [1 1 -1 1]
# [1 1 1 -1]
# #all 1 neg done
# [-1 -1 1 1]
# [-1 1 -1 1]
# [-1 1 1 -1]
# [1 -1 -1 1]
# [1 -1 1 -1]
# [1 1 -1 -1]
# #all with 2 neg done
# [-1 -1 -1 1]
# [-1 -1 1 -1]
# [-1 1 -1 -1]
# [1 -1 -1 -1]
# #all with 3 neg done
# [-1 -1 -1 -1]
# 
# 
# #test with 5
# # 1 with 0
# # 5 with 1
# # 10 with 2 
# # 10 with 3 
# # 5 with 4
# # 1 with 5 
# #the number of masks follow pascals triangle 
# 
# [1 1 1 1 1] 
# [-1 1 1 1 1]
# [1 -1 1 1 1]
# [1 1 -1 1 1]
# [1 1 1 -1 1]
# [1 1 1 1 -1]
# #1 done bring the rightmost negative up 1 then place all other negs adjacent to it on the right
# [-1 -1 1 1 1]
# [-1 1 -1 1 1]
# [-1 1 1 -1 1]
# [-1 1 1 1 -1]
# [1 -1 -1 1 1]
# [1 -1 1 -1 1]
# [1 -1 1 1 -1]
# [1 1 -1 -1 1]
# [1 1 -1 1 -1]
# [1 1 1 -1 -1]
# # 2 done
# [-1 -1 -1 1 1]
# [-1 -1 1 -1 1]
# [-1 -1 1 1 -1]
# [-1 1 -1 -1 1]
# [-1 1 -1 1 -1]
# [-1 1 1 -1 -1]
# [1 -1 -1 -1 1]
# [1 -1 -1 1 -1]
# [1 -1 1 -1 -1]
# [1 1 -1 -1 -1]
# #3 done
# [-1 -1 -1 -1 1]
# [-1 -1 -1 1 -1]
# [-1 -1 1 -1 -1]
# [-1 1 -1 -1 -1]
# [1 -1 -1 -1 -1]
# #4 done
# [-1 -1 -1 -1 -1]
# # 5 done
# 
# 
# 
# [1 -1 1 1 -1]
# [1 1 -1 1 -1]
# [1 1 1 -1 -1]

#terminate when all -1 values cannot move to the right unless it contacts

# =============================================================================

def pascals(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    start = [1,1]
    while n > 1:
        i,j = 0,1
        out = []
        while j < len(start):
            out.append(start[i]+start[j])
            i+=1 
            j+=1
        out.insert(0,1)
        out.append(1)
        start = out[:]
        n -=1
    return start
pascals(2)

