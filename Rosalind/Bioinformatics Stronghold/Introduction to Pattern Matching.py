# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 14:50:54 2022

@author: Shams
"""

#Introduction to Pattern Matching 

# =============================================================================
# Given: A list of at most 100 DNA strings of length at most 100 bp, none of which is a prefix of another.
# 
# Return: The adjacency list corresponding to the trie T for these patterns, in the following format. If T has n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. Each edge of the adjacency list of T will be encoded by a triple containing the integer representing the edge's parent node, followed by the integer representing the edge's child node, and finally the symbol labeling the edge.
# =============================================================================

#Ok so we know how the trie works now we need to implement a trie. 
#As we add the strings to the trie we can create the adjancy list at the same time as well
#The trie is made up of TrieNodes 

class TrieNode:
    def __init__(self, key=None, value=None):
        self.children = {}
        self.key = key
        self.value = value
        self.node_num = 1



class Trie(TrieNode):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self,sequences): #This method doesnt allow for the checking of substrings, initially for just adding a string but editted for rosalinds problem
        node = self.root
        counter = 1
        rosalind_list = [] #The Adjency List for rosalind problem
        for val in sequences:
            node = self.root
            for char in val:
                if char in node.children:
                    node = node.children[char]
                else:
                    new_node = TrieNode(char) #Create new node
                    node.children[char] = new_node #Add newly created node to children list of current node
                    parent = node.node_num
                    node = new_node #Set this node as the checking point
                    counter +=1 
                    node.node_num=counter
                    rosalind_list.append((parent,counter,char)) #The adjency list for rosalind problem
        return rosalind_list


test = Trie()
out = test.insert(['ATAGA','ATC','GAT'])
print(out)

def getdata(file):
    f = open(file)
    string_list = []
    for line in f:
        DNA_str = line.rstrip()
        string_list.append(DNA_str)
    trie = Trie()
    out = trie.insert(string_list) 
    t = open('out.txt','w+')
    for val in out:
        for char in val:
            t.write(str(char)+' ')
        t.write('\n')
    t.close()
    f.close()
    return out
        
getdata('test.txt')