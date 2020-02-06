# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:04:26 2020

@author: DRUELL
"""

string = input("Enter a string")

list1 = [] 
list2 = []

for char in string:
    if char not in list1:
        list1.append(char)
    else:
        list2.append(char)
        
print("List 1: ",list1)
print("List 2: ",list2)