# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:27:49 2016

@author: LydiaRoth
"""



from math import pi, sin

def H_eps(x, eps = 0.01):
   if x < -eps:
       value = 0
   if -eps <= x <= eps:
       value = 1/2 + x/2*eps + (1/2*pi)*sin(pi*x/eps)
   if x> eps:
       value = 1
   return value

def test_H_eps():
  if H_eps(-0.02)!= 0:
      print "error x"
  elif H_eps(-0.01) != 1/2 + -0.01/2*0.01 + (1/2*pi)*sin(pi*-0.01/0.01):
      print "error r"
  elif H_eps(0) != 1/2 + 0/2*0.01 + (1/2*pi)*sin(pi*0/0.01):
      print "error y"
  elif H_eps(0.02) != 1:
      print "error z"
  else:
      print "Everything is correct!"

test_H_eps()
