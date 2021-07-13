# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:09:34 2021

@author: Alson Nkuna
"""


def computepay(h, r):
    if h > 40:
        computed = h * r
        return computed
    else:
        print("No Overtime.")
    

h = input("Enter Hours:")
r = input("Enter Rate:")
hrs = float(h)
rate = float(r)
p = computepay(hrs, rate)
print("Pay", p)