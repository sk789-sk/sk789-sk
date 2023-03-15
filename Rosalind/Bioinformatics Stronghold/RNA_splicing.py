# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:14:42 2022

@author: Shams
"""

#RNA Splicing

# =============================================================================
# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
# 
# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
# 
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
# 
# 
# =============================================================================

from Bio import SeqIO

def makedic(file):
    f = open(file)
    translation_table = dict()
    for line in f:
        val_1 = line.rstrip('\n').rstrip(' ')
        key,value = val_1[0:3],val_1[4:]
        translation_table.update([(key,value)])
    f.close()
    return translation_table

def str2protein(string,codon_length,dic): #we make a protein from the sequence, now we need to provide the correct sequence
    prot = ''
    start = 0
    end = codon_length
    while end <= len(string):
        prot+= (dic.get(string[start:end]))
        start,end = start+codon_length,end+codon_length
    return prot[:-4] #last codon is stop so remove last 4

def removeexon(string,exon_list):
    exon_list.sort(key=len, reverse=True) #sort by len default is numeric i think idk. Make sure we dont lost larger exons by removing smaller ones that may break it that appear twice
    while exon_list:
        out = exon_list.pop(0)
        string = string.replace(out,'')
    string = string.replace('T','U')
    return string

  
def getdata(file): #Using Biopython to parse file
    stringlist = []
    records = list(SeqIO.parse(file,"fasta")) 
    for val in records:
        stringlist.append(str(val.seq))
    raw = stringlist.pop(0)
    out = removeexon(raw,stringlist)
    protstring=str2protein(out,3,makedic('RNA_translations.txt'))
    return protstring

out = getdata('rosalind_splc.txt')
print(out)
#out =removeexon(raw, exons)
#x = str2protein(out,3,table)
#print(x)

