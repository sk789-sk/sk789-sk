# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:17:05 2021

@author: Shams
"""

#degree array 
#In an undirected graph, the degree d(u) of a vertex u is the number of neighbors u has, or equivalently, the number of edges incident upon it.

#Given: A simple graph with n≤10^3 vertices in the edge list format.

#Return: An array D[1..n] where D[i] is the degree of vertex i.

#pretty much if the value shows up in the list then it has a neigher and an additional degree
#just run through the list once and make it so the value at the index increases by 1
#legit formatting is awful, just write to file everytime and upload file to keep it happy.

def degree(array): 
    degreearray = [0]*len(array)
    for val in array:
        degreearray[val-1] +=1
    return degreearray   
        
def getdata(file):
    f = open(file)
    t = open("out.txt","w+")
    #outarray = []
    #next(f) #skip the first line 
    #Lets read one line run the code then repeat until eof
    n = int(f.readline().split()[0])
    total = [0]*n
    allval = []
    for line in f:
        allval = allval + line.split()
    a = list(map(int,allval)) #list of integers
    for val in a:
        total[val-1] +=1
    #or just use degree function from earlier. 
    f.close()
    for val in total:
        t.write(str(val)+' ')    
    return 