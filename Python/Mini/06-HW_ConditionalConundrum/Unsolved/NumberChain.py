#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:51:16 2020

@author: Taslemun
"""

user = "y"

start_number = 1

while user == "y":

    user = input("How many numbers? ")
    
    for x in range(start_number, int(user), + start_number):
        
        print(x)
    
    start_number = start_number + int(user)

    user = input("Continue: (y)es or (n)o? ")





