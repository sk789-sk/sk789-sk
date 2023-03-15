# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:12:10 2021

@author: Shams
"""
#BFS problem, finding shortest path from node 1 to all other nodes in a graph
#Logic will be we take the start value and get the list of adjacent nodes.
#For those adjacent nodes we will assign the counter value to the corresponding index on return array.
#Pop the value and then append adjacent nodes for the popped node to the que.
#Repeat for all values that were from previous node

def Vlist(n): #Create the List of vertices
    Vlist = set()
    V_adjlist = {}
    for val in range(1,n+1):
        Vlist.add(val)
        V_adjlist.setdefault(val,[]) #Initialize with keys having empty lists
    return Vlist,V_adjlist

def adjacencylist(v1,v2,AdjList): #Adds an edge to adjacency list, directed so just 1 
    AdjList[v1] = AdjList[v1] + [v2]       
    return
     
#Better BFS implementation

def BFS2(adjlist,node): #Run DFS with an Adjlist and a starting Node   
    que = [node] #starting node
    d = 0 #initial distance from starting node is 0 
    distlist = [-1]*len(adjlist.keys())
    visitlist = set()
    while que:
        nodelvl = len(que) #the number of nodes on current lvl
        while nodelvl: #Since the que is changing in size as we pop and add values, we know when to increase depth value by looking at amount of nodes on the lvl
            x = que.pop(0)
            if x in visitlist:
                nodelvl -=1
            else:
                que+= adjlist[x]
                distlist[x-1] = d
                visitlist.add(x)    #Without the visitlist algo took forever to run/never finished
                nodelvl-=1
        d +=1 #new lvl so increment by 1
    return distlist
      
    
def getdata(file):
    f = open(file)
    t = open("out.txt","w+")
    n = int(f.readline().split()[0]) 
    V_list,V_adjlist = Vlist(n)
    for line in f:
        val = list(map(int,line.split()))
        adjacencylist(val[0],val[1],V_adjlist)
    y=BFS2(V_adjlist,1)
    
    for val in y:
        t.write(str(val)+' ')
    f.close()
    t.close()
    return 
