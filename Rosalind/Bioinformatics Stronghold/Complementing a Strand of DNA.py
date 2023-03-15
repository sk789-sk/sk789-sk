# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:55:21 2021

@author: Shams
"""

#Make a dictionary so i dont have to do potentionally 4 comparisons and just build the string working backwards

def rev_complement(string):
    Associated_Val = {'A':'T','T':'A','C':'G','G':'C'}
    complement = ''
    len_str = len(string)-1
    while len_str >= 0:
        complement += Associated_Val[string[len_str]]
        len_str -= 1
    return complement    