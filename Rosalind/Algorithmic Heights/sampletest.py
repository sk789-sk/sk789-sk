# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:49:38 2021

@author: Shams
"""

f = open("rosalind_2sum2.txt")
files = f.read()
files = files.split("\n")
files0 = files[0]
files0 = files0.split()

k = int(files0[0]) #num arrays
n = int(files0[1]) #array length

boolean = False

for z in range(1, k+1):
    if boolean == False:
        print('-1')
    boolean = False
    line = files[z]
    line = line.split()
    for x in range(0, n):
        if boolean == True:
            break
        else:
            current = int(line[x])
        for a in range(x+1, n):
            if int(line[a]) == (-1)*(current):
                print(str(x+1) + ' ' + str(a+1))
                boolean = True
                break