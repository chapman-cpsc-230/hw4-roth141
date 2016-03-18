# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:10:27 2016

@author: LydiaRoth
"""

def histogram(pass_list):
    print" in a function"
    for i in pass_list: 
        String = ""
        for j in range (i): 
            String = String + "*"
        print String    
histogram([4,9,13,5])       