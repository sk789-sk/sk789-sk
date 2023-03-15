# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:26:45 2021

@author: Shams
"""

#find a substing in a string:

def motifsearch(s,t): #S = main string t = substring
    sub1 = len(t)
    start = 0
    idx_list = []
    while start <= len(s): #alot of comparisons for each character point we might make the same number of comparisons as the lngth of the motif so O(nm)
        if s[start:start+sub1] == t:
            idx_list.append(start+1) #output wants indexing at 1
            start+=1
        else:
            start+=1
    return idx_list

#If i build a DFA it would look like this:
#I would need a way to keep track of indexing as I work my way through the states to return it on entering state 4
#Anytime i hit state 4 If i backtrack len(t)-1 I would hit the start of the index and can return that in array

#State     A     T     G     C
#0         1     0     0     0
#1(A)      1     2     0     0
#2(AT)     3     0     0     0
#3(ATA)    1     4     0     0 
#4(ATAT)   3     0     0     0
