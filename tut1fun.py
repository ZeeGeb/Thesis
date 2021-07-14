#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:00:46 2021
Tut 1 Question 3 of the Python Sessions for Hons.
@author: zee
"""

def func(a,b):
    ssum = a+b 
    diff = a-b
    prod = a*b
    quot = a/b
    
    return (ssum,diff,prod,quot)

print(func(8,2))

""" Question 4 """

def max_of_three(a,b,c):
    
    if(a > b and a > c):
        ans = a
    elif(b>a and b>c):
        ans = b
    else:
        ans = c
    return ans

print("The maximum is: ",max_of_three(2, 6, 7))

""" Question 5"""

def mult(a):
    
    if((7 % a == 0 or 3%a ==0) and (5%a == 0 or 8%a ==0)):
        return True
    else:
        return False 
    
print (mult(2))

"""Question 6"""

def poly(a,b,c,x):
    ans = a* (x**2) + b*x + c
    
    return ans

print("The polynomial answer is ",poly(2,4,1,1))

""" Question 7"""
def poly(a,b,c,x):
    a = 3
    c = 4
    ans = a* (x**2) + b*x + c
    
    return ans

print("The polynomial answer is ",poly(3,4,4,1))

"""Question 8"""


            