# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:04:57 2020

@author: DRUELL
"""

user_str = input("Enter string to remove puncs")

import string
for c in string.punctuation:
    user_str = user_str.replace(c,"")

print(user_str)
