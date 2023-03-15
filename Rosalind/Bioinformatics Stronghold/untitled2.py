# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:39:51 2021

@author: Shams
"""

'MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK'

import urllib3 
import requests 

def search(s): #given a string search for the n-glycosylation motif
#motif = N{P}[ST]{P}
#If we use a FSM we could do this linearly. 
#Simple brute way check first char if it is N, then check the next char, if it P then set counter to the p_idx+1 and restart
#If it is not equal to p then check the next index. If it is equal to S or T then check the next index. If not set counter to idx of itself +1
    v1 = 'N'
    v2 = 'P'
    v3 = 'S'
    v4 = 'T'
    c = 0
    idx_list = []
    while c <len(s):
        if s[c] == v1:
            if s[c+1] != v2:
                if s[c+2] == v3 or v4:
                    if s[c+3] != v4:
                        idx_list.append(c)
    
                        
    