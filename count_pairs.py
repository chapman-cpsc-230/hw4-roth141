# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:18:13 2016

@author: LydiaRoth
"""

def count_v2(dna,base):
    i = 0 
    for CA in dna:
        if CA == base:
            i += 1
        return dna.count(base)

dna = 'CAGGCACTTGATAT'
base= "CA"
n = count_v2(dna,base) 
print '%s appears %d times in %s' % (base,n, dna)    