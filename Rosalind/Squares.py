# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:05:04 2021

@author: Shams
"""

#Squares in a graph idea

#its in the notebook but lets say I have an adjaceny list.
#Ik for the starting node, i need 1 edge leaving the node and 1 edge returning to the node
#Ik my path will need 5 nodes and 4 edges 
#So my first edge will be the one leaving from node start to the first node on adjaceny list(i = 1)
#The last edge will be the one returning to the node to lets say the second value in the adjency list. (j =2)
#Now to complete the path we have to see if the first value in adjency list and second value in list share a common adjacent node
#If they do then great we have a cycle of length 4 and we can move on 
#If not, lets change the return node to the next value in the adjency list J+1.
#Iterate untill nothing left  
#If nothing here we change the leaving edge to the i+1.
#This way we go through a summation from 0 to E edges leaving from node 1 to check (E(E+1)/2)
#TO check if the 2 nodes have an adjacent node, if it is a matrix all I have to do is check the value in the same column or row, but at the right value

# If Matrix looked like this

#                   1 2 3 4 5 
#                 1 0 1 1 1 1
#                 2 0 0 1 0 1
#                 3 1 1 0 1 0
#                 4 0 0 1 0 1
#                 5 1 1 0 1 0
                
#to check if 2 and 4 shared a common adjacent node, i would look to see ok thisedge from 2 exists
#then i just slide down to row 4 and see if that value is 1. IF it is then yes they share and a cycle exists
#If not I look for the next non 0 value in 2 row. If i go through all the value in the 2 row with no hits, then no shared
#the 2 check exists are just access value so ill say O(1) and the number of comparisons is the Edges leading out of 2 subtract the ones leading to 1 and 4.
# E-2 potential comparisons 
#So the entire algo is E^3? This is only good since square, If it more than a square then it gets really bad since alot of branches to check

   
def square(adj_list,start):
    test_array = [start, 0,0,0,start] #A way to visualize
    i,j = 0,1
    while i < len(adj_list[start]):
        test_array[1] = adj_list[start][i]
        while j < len(adj_list[start]):
            test_array[3] = adj_list[start][j]
            #Now check to see if adjacent node between i,j
            
            
            
    


