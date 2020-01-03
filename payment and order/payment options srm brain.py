#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:34:03 2020

@author: kaustuvmohanty
"""

print(" PAYMENT OPTIONS:")
print(" --------------- ")
print("\n")
print(" Credit card: ")
print(" Debit card: ")
print(" Cash on Delivery ")
x = input("choose a payment option")
if x == "credit card":
    print(" the card number: ")
    y = input()
    print(" date of expiry in mm/yyyy")
    z = input()
    print(" cvv ")
    a = input()
elif x == "debit card":
    print(" the card number: ")
    y = input()
    print(" date of expiry in mm/yyyy ")
    z = input()
    print(" cvv ")
    a = input()
else: x == "cash on delivery"
    
print("payment successful")




    
    

    
    
    
    
