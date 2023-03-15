# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:52:53 2021

@author: Shams
"""

        
#I could just implement it in the array and just shifting around in the array until i get to where i need    
#future write the output to a file and then go, copy pasting text gave me errors with formatting since my code was right but the answer was "wrong"

#does the searching for a value in a list in nlogn time        
def binary_search2(m,array):
    start = 0                #index 0
    end = len(array) - 1     #index last
    
    while start <= end:      #loop until starting point would be larger then ending point. Would mean empty array
        midpoint = (start+end)//2 #splitting point this value changes and adjusts my start and end
        if array[midpoint] == m:   #we found the value so we return index
            return midpoint
        elif array[midpoint]>m:     #the value is in the lower half from this point
            end = midpoint -1        #leave the starting point as is, but change the end point of the area to split -1
        else:                       #only other scenario is value is in the highe rhalf from mid point
            start = midpoint+1      #leave the ending as is and change the start to split + 1
    return -1                       #if we leave the loop then value isnt in the list and return -1        
            

#takes the file inputs and does the searching of every value in the array and returns index list should be mnlogn time    
def Rosalind2(n,m,Search_Array,Int_List):
    #n is the size of the array to be searched
    #m is the size of the list of integers to be looking for
    Loc = [0]*m  #create a list of size m to store the locations  
    i = 0      #initialize i 
    while i<m: #go thourh ght list 
        idx_of_int = binary_search2(Int_List[i],Search_Array)
        if idx_of_int == -1:                   #this loops is just to meet the index criteria  starting from 1
            Loc[i] = idx_of_int
        else:
            Loc[i] = idx_of_int+1
        i +=1
    return Loc

def get_data(filename): #return the stuff in want in a tuple
    data = open(filename)
    n = int(data.readline())
    m = int(data.readline())
    Search_Array = data.readline().split(" ")
    Search_ints = data.readline().split(" ")
    counter_int = 0 
    counter = 0
    while counter_int < len(Search_ints):
        Search_ints[counter_int] = int(Search_ints[counter_int])
        counter_int +=1
    while counter < len(Search_Array):
        Search_Array[counter] = int(Search_Array[counter])
        counter +=1    
    data.close()
    return n,m,Search_Array,Search_ints
    
def formatout(x): #gives me the output file, hsould
    x = str(x)
    out_val = x.replace(',','').replace('[','').replace(']','') #delete the commas
    f = open('output.txt', "x")
    f.write(out_val)
    f.close()