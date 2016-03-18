# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:42:15 2016

@author: LydiaRoth
"""
def histogram(pass_list):
    print" n | Data"
    print"---+----------------"
    for i in pass_list: 
        String = ""
        for j in range (i): 
            String = String + "*"
        print len(String)," | " , String  
histogram([4,9,13,5]) 