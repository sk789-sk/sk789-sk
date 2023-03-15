# -*- coding: utf-8 -*-
"""
Created on Tue May 25 00:41:36 2021

@author: Shams
"""

#make the Dictionary for RNA codons

def makedic(file):
    f = open(file)
    translation_table = dict()
    for line in f:
        val_1 = line.rstrip('\n').rstrip(' ')
        key,value = val_1[0:3],val_1[4:]
        translation_table.update([(key,value)])
    f.close()
    return translation_table    

def str2protein(string,codon_length,dic):
    prot = ''
    start = 0
    end = codon_length
    while end <= len(string):
        prot+= (dic.get(string[start:end]))
        start,end = start+codon_length,end+codon_length
    return prot[:-4] #last codon is stop so remove last 4
        