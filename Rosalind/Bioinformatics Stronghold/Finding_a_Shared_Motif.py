# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:29:47 2021

@author: Shams
"""

from Bio import SeqIO
#Finding a Shared Motif

# =============================================================================
# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# 
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
# =============================================================================

#I think the best way to go about this will be to create a DFA for on string. 
#We then run the next sequence through the DFA to search for the largest substring.
#That substring becomes the new max substring. 
#We then run the subsequent strings through the DFA shortening the longest substring until we go through all the strings
#Whatever is left is the largest common substring 
#Scratch that idea, misread what I wanted to do.

#I think instead we should take the shortest string and then build a tree out of it with all possible strings 
#Suffix tree/trie 
#Example ATACA tree check notes. We can than 

#Making a trie in a slow way would be striaghtforward I think.
#We first insert the entire string into the trie. We then insert each substring so we do n insertions.
#The branching factor for the tree would be the size of the alphabet and it would grow pretty fast
#Once we have the first string inserted we insert subsequenct strings by following down the path of the tree. 
#If we hit a point where theres no branch to follow then we will insert the rest of the string letter by letter as children to that point
#Ex: Bananas
#first insertion is B - A - N - A -N - A - S
#Next we insert ANANAS. We start at the root node and search for an A connection. There is none so we add in a node to A and then the rest of the string
#then we insert NANAS. Same logic as ANANAS happens
#Then we insert ANAS. We search for the A and find it. This A is not eh node and we look for a child node of N which we find and then A then finally S which we dont so we create a new node. 

#Searching the node is taking a substring and then 

#ex: GATTACA, TAGACCA, ATACA 

#A --> T --> A --> C ---> A
class TrieNode:
    def __init__(self, char = ""):
        self.char = char
        self.children = {}
        self.is_end = False
        # self.counter = 0


class Trie:

    def __init__(self): #setup trie with root node
        self.root = TrieNode()
    def insert(self, word: str): #Add a string into the trie
            """
            Inserts a word into the trie.
            """
            node = self.root
            i = 0
            while i < len(word):
                node = self.root
                for char in word[i:]:
                    if char not in node.children:
                        new_node = TrieNode(char)
                        node.children[char]=new_node
                        node = new_node
                    else:
                        node = node.children[char]
                i+=1
    def search(self,word): #returns if a sequence is in the word, if not returns the largest subsequence
        node = self.root
        subseq = ''
        for char in word:
            if char not in node.children:
                return subseq
            else:
                node = node.children[char]
                subseq +=char
        return subseq
    
    def clear(self):
        node = self.node
        self.childern.clear()
    
    def readtree(self):
        node = self.root


        
def largestsub(Trie,word):
    i = 0
    stringarray = []
    while i < len(word):
        out = Trie.search(word[i:])
        stringarray.append(out)
        i +=1
    return stringarray

def largestcommon(*arg):
    t1 = Trie()
    for val in arg:
        t1.insert(val)
    return t1

def allperm(string):
    total = ((len(string)**2)+len(string))/2
    out = set()
    i = len(string)
    while i > 0:
        j = 0
        while i+j <= len(string):
            sub = string[j:i]
            out.add(sub)
        i -=1
  
 

#Now how do we make sure we get the largest subsequence 
#There is the idea where we all all strings into the trie with markers for which substrings belong to which string. 
#Find the deepest node that has all the following string terminators as children would be the largest substring
#That would require more work I will fix put an addition for that in the future. I would need to implement a way to read the tree from the leafs up. 

#This idea is slower but should work.
#We create a trie for 1 and then check the for all common substrings witht he search function
#We then create a trie of the next substring. We have a list of acceptable substrings from earlier and now we search all the strings in the list with search. Alot of wasted overlap
#Like if we find TACA ofc we will find ACA CA A C and this is gonna balloon fast.



#Been a while since I looked at this so lets try again from scratch
#We can do this in a simpler way 
#First find all the substrings of 1 string and search to see if those are in another
#Take the ones that made the cut and repeat with the next substrings
#This way we get all substrings for 1 string and just do repeated in which is how fast idk? O(n)? 

def allsub(value):
    l = len(value)
    substring_set = set()
    while l > 0:
        start = 0
        end = start + l
        while end <= len(value):
            subs = value[start:end]
            start +=1
            end +=1
            substring_set.add(subs)
        l -=1
    return substring_set

def commonsubstrings(string,stringlist):
    newlist = set()
    for val in stringlist:
        if val in string:
            newlist.add(val)
    return newlist

def max_common_substrings(string_list):
    x = allsub(string_list[0])
    for val in string_list[1:]:
        x = commonsubstrings(val,x)
    return max(x,key=len)

def getdata(file): #Using Biopython to parse file
    stringlist = []
    records = list(SeqIO.parse(file,"fasta")) 
    for val in records:
        stringlist.append(str(val.seq))
    out = max_common_substrings(stringlist)
    return out

allsub('abcd')