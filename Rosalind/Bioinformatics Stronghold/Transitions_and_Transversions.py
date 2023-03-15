# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:43:13 2022

@author: Shams
"""
#Transitions and Transversions


#One Idea i have is overkill i think, but i replace all the bases with numeric values
#let the purines A,G equal even numbers 0 and 2
#let the pyrimadines T,C equal odd numbers 1 and 3
#Now I subtract the 2 strings from each other digit by digit and get a new string
#Now I read the string potential values
# 0 = the 2 bases were equal to each other 
# -2,2 = if the value is even then we had a transition purine to purine or pyrimadine to pyrimadine
# 1,-1,3,-3 = if the value is odd then we had a transversion 

#this way in 1 pass we can get values of transversions/transitions without comparison at each digit
#but we need to replace all the values which would probably take a while? 
#Maybe I can make my own alphabet of the 4 and set subtraction rules for it. 

from Bio import SeqIO

def TTratio(string):
    strings = []
    for val in string:
        val = val.replace('A','0')
        val = val.replace('G','2')
        val = val.replace('C','3')
        val = val.replace('T','1')
        strings.append(val)
    i = 0
    transversion = 0
    transition = 0
    good = 0
    while i < len(string[0]):
        if (int(strings[0][i])-int(strings[1][i]))%2 ==1:
            transversion +=1           
        elif (int(strings[0][i])-int(strings[1][i])) ==0:
            good +=1
        else:
            transition +=1
        i+=1
    return (transition/transversion)

def getdata(file): #Using Biopython to parse file
    stringlist = []
    records = list(SeqIO.parse(file,"fasta")) 
    for val in records:
        stringlist.append(str(val.seq))
    out = TTratio(stringlist)
    return out

