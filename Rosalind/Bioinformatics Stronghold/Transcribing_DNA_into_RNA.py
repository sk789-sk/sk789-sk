# -*- coding: utf-8 -*-
"""
Created on Thu May 20 18:11:03 2021

@author: Shams
"""

def transcribe(string):
    RNA = ''
    for i in string:
        if i == 'T':
            RNA += 'U'
        else:
            RNA += i
    return RNA        