# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:13:18 2021

@author: Shams
"""

#the idea heres is to calculate the punnet square for any mating possibility
#then calculate the odds of that mating possibility occuring
#then just find the total probability from that

def punnet(x,y): #find the punnet square for 2 strings #I could just for down the characters in 1 and combine with all in second
    #since this is 2x2 punnet square i can calculate values ahead of time and its just a probability prooblem but thats not generic
    #this only works for a 2x2 punnet, didnt add anything for proper splitting and etc.
    #returns the odd of a phenotype displaying negative trait.
    expression = []
    for val in x:   #creates a list of all possible genotypes
        for char in y:
            expression.append(val+char)
    check = x.lower()
    recessive = 0
    for loc,vals in enumerate(expression): #iterate through the list and look for homozygous recessive
        if expression[loc] == check:
            recessive +=1
    return 1-(recessive/len(expression))       

#for the punnet square is calculates a 2x2 just fine so I could use it on lets say 2 allele and solve it recursively

def pop_prob(dom,heter,rec): #absolutely disgusting way to do this
    D = 'AA'
    H = 'Aa'
    R = 'aa'
    total_pop = dom+heter+rec
    t2 = total_pop -1
    
    #odds at each stage
    dom1 = dom/total_pop
    heter1 = heter/total_pop
    rec1 = rec/total_pop
    
    
    #odds of a pair happening
    dd = dom1*((dom-1)/(t2))
    dh = dom1*((heter/t2)) + heter1*(dom/t2)
    dr = dom1*((rec/t2)) + rec1*(dom/t2)
    hh = heter1*((heter-1)/t2)
    hr = heter1*(rec/t2) +rec1*(heter/t2)
    rr = rec1*((rec-1)/t2)
    
    total = [ dd*punnet(D,D), dh*punnet(D,H),dr*punnet(D,R),hh*punnet(H,H),hr*punnet(H,R),rr*punnet(R,R)]
    return sum(total)

#pop_prob(2,2,2) 