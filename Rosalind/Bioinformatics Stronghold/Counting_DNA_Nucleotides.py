# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:42:22 2021

@author: Shams
"""

def nucleotide_count(string):
    out_array = [0,0,0,0] # [A C G T]
    i = 0 #counter
    while i <= len(string) -1:
        if string[i] == 'A' :
            out_array[0] +=1
        elif string[i] == 'C':
            out_array[1] +=1
        elif string[i] == 'G':
            out_array[2] +=1
        elif string[i] == 'T':
            out_array[3] +=1
        i +=1
    return out_array        
        
        
            