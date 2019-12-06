# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:49:57 2019

@author: bashi
"""

test = "abaab"

def palindrome(s):

    # function to reverse a string 
    def reverse(word):
        
        str = "" 
        for i in word: 
            str = i + str
        return str
    
# to find all substrings
    alll=[]
    for length in range(1, len(s)):
        
    # Loop over possible start indexes.
        for start in range(0, len(s) - length + 1):
        # Take substring and print it.
            part = s[start:length + start]
            alll.append(part)
#print(alll)
    
    #  checking if a substring is equivalent to its reversed form   
    final = []
    for sub in alll:
        if sub == reverse(sub) and len(sub) > 1:
            final.append(sub)
    print ('The no of distinct palindromes in the string is:', len(final))
    
    
    
    
