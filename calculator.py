#https://github.com/arianmayi/Lab11_AM_NT.git
#Arian Mayi - Partner 1
#Ngoc Tieu - Partner 2

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except TypeError:
        raise ValueError

def hypotenuse(a,b):
    try:
        return math.hypot(a,b)
    except TypeError:
        raise ValueError

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError
    return b/a

def logarithm(a,b):
    if a <= 1 or b <= 0:
        raise ValueError
    return math.log(a,b)

def exponent(a,b):
    a**b




