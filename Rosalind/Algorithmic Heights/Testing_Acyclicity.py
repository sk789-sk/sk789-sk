# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 17:20:18 2021

@author: Shams
"""

#Testing Acyclicity 

# =============================================================================
# Given: A positive integer k≤20 and k simple directed graphs in the edge list format with at most 103 vertices and 3⋅103 edges each.
# 
# Return: For each graph, output "1" if the graph is acyclic and "-1" otherwise.
# =============================================================================

#If the number of edges and vertices are equal then there has to be a cycle.
#If the number of edges is less than the vertices there may still be a cycle if the graph is disconnected
#I think the way to check would be to run DFS and see if we attempt to check a node that has already been visited.
#But first we can eliminate all graphs with equal V and E. I dont think the conditions allow for a E > V. 

def Vlist(n): #Create the List of vertices
    Vlist = set()
    V_adjlist = {}
    for val in range(1,n+1):
        Vlist.add(val)
        V_adjlist.setdefault(val,[]) #Initialize with keys having empty lists
    return Vlist,V_adjlist

def adjacencylist(v1,v2,AdjList): #Adds an edge to adjacency list
    AdjList[v1] = AdjList[v1] + [v2]
    #AdjList[v2] = AdjList[v2] + [v1]          
    return


def DFS2(adjlist,node, visit): #Run DFS with an Adjlist and a starting Node and a set of visited nodes    
    if  visit[node-1] == 0:
        visit[node-1] += 1
        for val in adjlist[node]:
            DFS(adjlist,adjlist[node],visit)
    if node not in visit:
       visit.add(node)
       for val in adjlist[node]:
         DFS(adjlist,val,visit)
    else: 
        return [-1]
    return [1]


def DFS(adjlist,node, visit = set()): #Run DFS with an Adjlist and a starting Node and a set of visited nodes    
    if node not in visit:
        visit.add(node)
        for val in adjlist[node]:
            DFS(adjlist,val,visit)
    return visit
# the way this is setup it just returns the based on whether or not the starting node is in the visited list, so itll always return 1.
#What if we just do DFS, and instead we keep the visit set outside the array and return a value if value is >1
#Boolean array for all the nodes, once we visit we toggle value to 1
#If we attempt to toggle a value once its 1 we know we have a backedge
#We want to terminate right there then instead of recursing back. 


def tcycle(adj_list): #this would be assuming we have one that is fine
    V_array = [0]*len(adj_list)
    DFS(adj_list, 1,V_array)
    
    DFS(adj_list, 1)
    return 

test = { 4: [1] , 1: [2] , 2:[3], 3:[]}
test2 = { 4: [1] , 1: [2] , 2:[3], 3:[1]}
x = DFS(test,1,visit = set())
y = DFS2(test2,4,visit = [0]*len(test2))
z = 9