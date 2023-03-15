# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:19:25 2021

@author: Shams
"""

#Independent alleles, most of the owrk was done hand to come to the logic.

#Probability that at least n people will exhibit AaBb genotype:
#this is equal to the P(Aa)*P(Bb)
#P(Aa) = P(P1A and P2a) + P(P1a and P2A) #we will take P1 to be the mate of choise so AaBb genotype
#then P(Aa) = P(P1A)P(P2a)+P(P1a)P(P2A)
#Then the P1A and P1a are 1/2 since we always have that parent then
#P(Aa) = 1/2(P(P2a)+P(P2A)) P2a and P2A are the only 2 cases so together that is a probability of 1
#Therefore the probability of P(Aa) is equal to 1/2
#Same logic is extended for P(Bb) so the probability of P(AaBb)=1/4
#Drawing out 9 punnet squares for all potential genotypes will show this as well

#Since i know the probability of any individual to be AabB in a generation is .25 then this becomes a binomial equation problem
#Ik odds of this happening, number of trials 2^k, and number of successes I want

#Binomial probability calculator is all the combinations*(succ)^k*(1-succ)^n-k
#then we just iterate it from num succ required to all succ to get total probability.
from math import factorial as fac

def probn(n,k):
    total = 2**k #number of trials
    prob = 0
    while n<=total:
        combos = fac(total)/(fac(n)*fac(total-n))
        prob += combos*((.25)**n)*((.75)**(total-n))
        n +=1
    return prob

probn(1,2)