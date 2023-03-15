# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 08:01:14 2021

@author: Shams
"""

#Implement Djikstra's algorithm.
#Check notebook for algo summary or look online.
#we will try to do it without libs and then with libs also

#import numpy as np
#import pandas as pd
#import heapq as hq
from queue import PriorityQueue

#So the logic will be we get an input node and an adjancy list.
#We keep a track of verteices visited, distance from the start node, and previous node
#Set the distance to all other nodes as infinity and the start node as 0.
#From the Shortest distance list we take the value with the smallest value and add it to the priority que
#When the priority que is empty that means we have visited all reachable nodes
#We will add that value ot the priority que.
#Pop the value form the priority que and add the adjacent vertices to the priority que
#the smallest value would have to be an adjacent node at all times.

def Djikstra(adj_list,start):
    visited = set()
    pq = PriorityQueue()
    distance = [float("inf")]*len(adj_list)
    distance[start-1] = 0
    pv = [0]*len(adj_list)  
    pv[start-1] = None
    pq.put((0,start))
    path_length = 0 
    while pq.empty() == False:
        vert = pq.get()[1]   #Ok so know i have the vertex of interest
        #if vert in visited: #If we already visited it go again 
        #   vert = pq.get(block = True, timeout = 2)[1]  #get from empty queue breaks it 
        visited.add(vert)
        path_length =distance[vert-1]
        for val in adj_list[vert]:
            if val != ():                 
                dist_t = val[1] + path_length #Assume its (node, length)
                if dist_t <= distance[val[0]-1]:
                    distance[val[0]-1] = dist_t #We update the shortest path now
                    pv[val[0]-1] = vert  #previous value is the old vertext now
                if (val[0] in visited) == False:
                    pq.put((distance[val[0]-1],val[0]))   #Adding the adjacent vertex to priority que
            else:
                break
    distance = [x if x != float('inf') else -1 for x in distance] #conv. inf to -1 for no direct path
    return distance, pv

#The issue is that i still have the old value in the priority que when it should be removed for the new one
#Other than that this algo looks to work, at least for the 2 small 4 and 5 node graph I am testing with.
#Test with rosalind set once, it worked!
#At the end im running a ton of iterations or now reason since I have a PQ with unnecessary value. 
#heapq would be better it think, but i didnt look into its documentation. 
#i could use my heap algo to make a pq also.
#now to turn the raw data set into and adj-list



def adj_list(v1,v2,weight,adjlist): #fix this bit
    adjlist[v1].append((v2,weight))
    return adjlist

def getdata(file):
    f = open(file)
    n = int(f.readline().split()[0]) 
    adjlist = {}
    for val in range(1,n+1):
        adjlist.setdefault(val,[])
    for line in f:
        val = list(map(int,line.split()))
        adj_list(val[0],val[1],val[2],adjlist)
    x,y =Djikstra(adjlist,1)
    f.close()
    t = open('out.txt', 'w+')
    for val in x:
        t.write(str(val)+' ')
    return x,y 

#test = {1: [(2,4),(3,6),(4,8)],2: [(4,1)],4:[(3,9)],3:[()]}
#Djikstra(test,1)
breaks = { 1: [(2,1),(4,5),(5,7)], 2: [(3,1)], 3: [()], 4: [(3,2),(5,1)], 5: [()]}
Djikstra(breaks,1)

