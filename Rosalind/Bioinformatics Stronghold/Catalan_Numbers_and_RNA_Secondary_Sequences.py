# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:42:09 2021

@author: Shams
"""

#Catalan Numbers and RNA Secondary Sequences

# =============================================================================
# Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
# 
# Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.
# =============================================================================

#Catalan Number
#Cn = summation(k=1,n) of C(k-1) * C(n-k)

#product of (n+k)/k from k =2 to N

def catalan(n):
    total = 1
    k = 2
    while k<=n:
        total  *= (n+k)/k
        k+=1
    return total % 1000000
