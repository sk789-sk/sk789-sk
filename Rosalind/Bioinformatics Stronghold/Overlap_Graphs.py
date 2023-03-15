# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:44:18 2021

@author: Shams
"""

#Overlap Graph see notebook for explanation

#First we have to load the data into a dictionary. The rosalind tag is the key and the string is the associated vlue
#The sample output makes it seam not really an adjaceny list.

#Were gonna use biopython to importing the data properly
#We could do something to paste it everytime but nty

from Bio import SeqIO

def getdata(file):
    input_file = open(file)
    my_dict = SeqIO.to_dict(SeqIO.parse(input_file, "fasta"))
    k = 3
    out = overlapgraph(my_dict,k)
    input_file.close()
    t = open("out.txt","w+")
    for val in out:
        for val in val:
            t.write(str(val)+ ' ')
        t.write('\n')
    return out


def overlapgraph(s_dict,k): #O(key^2)
    tuple_list = [] 
    for key in s_dict: #(O(k)ey)
        #suffix = s_dict[key][-k:] #get the suffix of interest if list
        suffix = s_dict[key].seq[-3:] #We used biopython to load the values so they are seq types
        for val in s_dict: #O(key)
            if val != key:
                #prefix = s_dict[val][:k]
                prefix = s_dict[val].seq[:k]
                if suffix == prefix:
                    tuple_list.append((key,val))
    return tuple_list
                
#test_dict = {'Rosalind_0498': 'AAATAAA' , 'Rosalind_2391': 'AAATTTT', 'Rosalind_2323': 'TTTTCCC', 'Rosalind_0442': 'AAATCCC', 'Rosalind_5013': 'GGGTGGG'}

#overlapgraph(test_dict,3)