# -*- coding: utf-8 -*-
"""
Created on Wed May 26 18:45:09 2021

@author: Shams
"""

#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

def hamm(s,t):
    counter = 0
    for x,idx in enumerate(s):
        if s[x] != t[x]:
            counter += 1
    return counter
            
        