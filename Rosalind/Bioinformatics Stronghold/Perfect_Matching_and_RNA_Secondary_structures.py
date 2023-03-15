# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:02:06 2021

@author: Shams
"""

#Perfect Matchings and RNA Secondary Structures

#Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

#Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

#The AU will pair togther, and the CG will pair together. So we wanna see all the combinations where 
#AU pair and CG pair and then combine the 2. In the example with 10 nucleotides, we have 3 AU pairs and 2 CG pairs
#3 AU pairs can form 3 factorial combinations, and 2 CG pairs can form 2 factorial combinations (6,2)
#The total number of perfect matches then would be 3! *2!. If we think of it as 2 different graphs, 1 au and 1 cg each graph has n! perfect pairings
#This logic works for any string, so all we have to do is see how many pairs we have in the string, find the factorial of those values and multiply them together
#each graph pair is a bipartate graph

from math import factorial

def matches(n):
    i = 1
    total = 1
    if n %2 == 1:
        return 'no perfect match'
    while i < n:
        total = total*i
        i +=2
    return total
        
def perfmatch(s): #O(n)
    AU_c = 0
    CG_c = 0
    for val in s:
        if val == 'A':
            AU_c +=1
        if val == 'C':
            CG_c +=1
    return factorial(AU_c)*factorial(CG_c)

perfmatch('AGCUAGUCAU')