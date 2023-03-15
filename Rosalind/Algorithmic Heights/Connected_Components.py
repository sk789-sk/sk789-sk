# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:51:56 2021

@author: Shams
"""

#Connected COmponents problem, given a edge list format graph return how many connected components there are
#First we have a list of all the vertices 
#We pick a vertex, RUN DFS and get a visited nodes list.
#We remove these nodes from the vertices list, and run again at a non 0.
#Repeat until all values in the list are gone, 
#Use a set to just subtract them easily I think. 

#Create the set

def Vlist(n): #Create the List of vertices
    Vlist = set()
    V_adjlist = {}
    for val in range(1,n+1):
        Vlist.add(val)
        V_adjlist.setdefault(val,[]) #Initialize with keys having empty lists
    return Vlist,V_adjlist

def adjacencylist(v1,v2,AdjList): #Adds an edge to adjacency list
    AdjList[v1] = AdjList[v1] + [v2]
    AdjList[v2] = AdjList[v2] + [v1]          
    return

def DFS(adjlist,node, visit = set()): #Run DFS with an Adjlist and a starting Node and a set of visited nodes    
    if node not in visit:
        visit.add(node)
        for val in adjlist[node]:
            DFS(adjlist,val,visit)
    return visit
#Now we can run DFS from a starting node and get back the connected nodes
#Remove all these nodes form the 


def getdata(file):
    f = open(file)
    n = int(f.readline().split()[0]) 
    c = 0 #Counter for how many connected components
    visit = set()
    V_list,V_adjlist = Vlist(n)
    for line in f:
        val = list(map(int,line.split()))
        adjacencylist(val[0],val[1],V_adjlist)
    
    while bool(V_list): #start removing connected components from the list
        out = DFS(V_adjlist,V_list.pop(),visit)
        c +=1
        V_list -=out
    return c

#l_test = {1: [2,3], 2: [4,5], 3:[6], 4: [], 5:[], 6:[]}
#t2 = { 1: [2], 2:[8], 4:[10], 6:[10], 10:[6],8:[2]}
#DFS(t2,1)

getdata('test2.txt')
#getdata('rosalind_cc.txt')

#DFS(l_test,1)