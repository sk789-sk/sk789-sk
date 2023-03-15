# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:34:10 2021

@author: Shams
"""

def GCcalc(string):  #O(m) length of string
    CG_cont = 0
    for x in string:
        if x == 'C' or x=='G':
            CG_cont +=1
    return float((CG_cont/len(string))*100)    

def dataload(file): #load the data into a dictionary where I can get key and sequence, dumb way to do it but first thing to pop into my head
    storage = dict()
    fasta = open(file,'r')
    current_key = ''
    for line in fasta:
        c_line = line.rstrip("\n")   #get rid of newlines
        if c_line[0] == '>':
            storage[c_line[1:len(c_line)]] = ''   #get rid of >
            current_key = c_line[1:len(c_line)]   #store the key
        else:
            storage.update({current_key: storage.get(current_key)+c_line}) #updating value with assocaited key
    fasta.close()
    return storage
#really what i should do is the same where i stip the line and do the calculation and store the results in a list or tuple and then see

#dataload('fastatest.txt')        

#go through dictionary with key and get the GC value of the string associated 
def largest_GC(values):
    key_val = []
    for keys in values.keys(): #O(n) keys
        content = GCcalc(values.get(keys)) #O(m) length of string
        key_val.append((keys,content))
    return key_val            

#O(mn) complexity

#something better would be to laod the datafile line by line, get ID and content then calculate value
#throw out the data and then repeat 