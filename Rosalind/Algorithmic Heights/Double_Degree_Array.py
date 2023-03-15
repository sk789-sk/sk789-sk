# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:44:59 2021

@author: Shams
"""
#Double Degree Array Problem, check notebook for reasoning
#Make a dictionary of keys(vertex), and the the values is a list/set of attached vertices
#Make an array for the degree of each vertex
#For each key, iterate over the list of values in the associated list, and get the associated degree of the key
#and then sum that value and add it to a new array. Using index to indicate the value point
#lets try to do it while reading in the values line by line 


def degree(array): #Calculate the degree of each vertex, just find how many times each value appears in array(edge list)
    degreearray = [0]*len(array)
    for val in array:
        degreearray[val-1] +=1
    return degreearray

#We will already have a dict with all the keys from reading of the first char
def adjacencylist(v1,v2,vertexdict): #Adds an edge to adjacency list, don't think any duplicates so list is fine instead of set
    if vertexdict[v1] == None:
        vertexdict[v1] = [v2]
    else:
        vertexdict[v1] = vertexdict[v1] + [v2]
    if vertexdict[v2] == None:
        vertexdict[v2] = [v1]
    else: 
        vertexdict[v2] = vertexdict[v2] + [v1]          
    return

def doubledegree(adjlist,deglist): #Takes an adjency List, and corresponding list of degrees for each vertex and returns the  sum of the degrees for all neighers for each vertex
    out = [0] * len(adjlist.keys())
    for x in adjlist.keys():
        cumsum = 0
        if adjlist[x] == None:
            out[x-1] = 0
        else:
            for values in adjlist[x]:
                cumsum = cumsum + deglist[values-1]
                out[x-1] = cumsum
    return out

def getdata(file): #Does the the necessary processing
    f = open(file)
    t = open("out.txt","w+")
    n = int(f.readline().split()[0]) #number of vertices
    total = [0]*n #deglist
    vertexdict = {} #adjacency list
    for x in range (1,n+1):
        vertexdict.setdefault(x)
    allval = []
    for line in f:
        val = list(map(int,line.split()))
        adjacencylist(val[0],val[1],vertexdict)
        allval = allval + val
    for val in allval:
        total[val-1] +=1
    f.close()
    #Ok at this point i have my adjancy list and degree of all vertices
    final = doubledegree(vertexdict, total)
    for val in final:
        t.write(str(val)+' ')    
    return vertexdict,total

