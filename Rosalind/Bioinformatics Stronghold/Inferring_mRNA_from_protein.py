# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:04:08 2021

@author: Shams
"""

from Amino_Acid_2_codon_cnt import Amino_Acid2codon

def mRNAfromProt(protString):
    totalnum = 3 #starting at 3 since 3 stop codons
    for x in protString:
        q_x = x #dic key is 'val' but x out is just a val, if i let it equal to a var then i get the quotes, stupid but whatever way to do it
        out = Amino_Acid2codon[q_x]
        totalnum *= out
        if totalnum > 1000000: #divison is expensive so i could let the int get as large as possible then take modulo
            totalnum %= 1000000
    return totalnum        

#oops mistyped and let W = 2 instad of 1
    