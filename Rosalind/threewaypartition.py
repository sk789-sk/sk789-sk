# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:56:04 2021

@author: Shams
"""

#3 way partition
#All the values equal to the partition point should be together
#[(values < array[0]), values == array[0], values > array[0] ]

def threewaypartition(array):
    idx,offset = 0,1 #keep track of initial value and what we are conmparing against
    while (idx + offset) < len(array): #We stop once we hit the array length
        if array[idx] > array[idx+offset]: #If start value is larger we pop the compared value to the front of the list
            array.insert(0,array.pop(idx+offset))
            idx +=1 #increase index by 1 since we popped a value to list start
        elif array[idx] == array[idx+offset]:
            array.insert(idx,array.pop(idx+offset)) #if values are equal and we want to keep it together so pop it and place it where the old index used to be
            idx +=1 #increase idx by 1 since we popped a value
        else: #only has value to be less then
            offset+=1 #we just push the offset by 1 to compare to next value.
    return array
#i think every insert is O(n) time since we shift all array points so pretty slow, unless linked list?
    

#data input and sorting 
def getdata(file):
    f = open(file)
    data = f.readlines()
    a = list(map(int,data[1].split()))
    out = threewaypartition(a)
    f.close()
    f= open("out.txt","w+")
    for value in out:
        f.write(str(value)+ ' ')
    return out 

#array = [7, 2, 7, 5, 6, 1, 3, 9, 4, 8, 4, 1, 7, 9, 3] 
#threewaypartition(array) 