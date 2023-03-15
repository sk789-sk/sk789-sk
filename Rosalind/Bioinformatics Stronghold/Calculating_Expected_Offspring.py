# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:39:57 2021

@author: Shams
"""

from Mendels_First_Law import punnet 

def EVdom(poplist): #Poplist structure[AA-AA,AA-Aa,AA-aa,Aa-Aa,aa-Aa,aa-aa]
    genotype_list = ['AA-AA','AA-Aa','AA-aa','Aa-Aa','aa-Aa','aa-aa']
    #I dont need to calculate punnet since i can just preload each value but figured ill use it since i made it
    EV_list = []
    for x,pair in enumerate(genotype_list):
        EV = 2*punnet(genotype_list[x][0:2],genotype_list[x][3:])
        EV_list.append(EV)
    #print(EV_list)
    for y,pair in enumerate(poplist): #when i did for x in list i started at x = 1 and it all got screwy
        EV_list[y] = poplist[y]*EV_list[y]
    return sum(EV_list)    
    