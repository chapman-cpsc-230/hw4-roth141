# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:14:39 2016

@author: LydiaRoth
"""

def H(x):
    if x <0:
        value =0 
    if x>=0:  
        value = 1
    return value    
    
def test_H(): 
    if H(-10)!= 0 :
        print "error" 
    elif H(10**25) !=0: 
        print "error"
    elif H(-10**-15) !=0: 
        print "error"
    elif H(0) !=1: 
        print "error"    
    elif H(10**-15) !=0: 
        print "error"  
    elif H(10) !=1: 
        print "error"    
        
print "Good to Go"       