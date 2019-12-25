# -*- coding: utf-8 -*- 
"""
Created on Thu Dec 19 11:51:10 2019

@author: Jeremy Scharf
"""

import string



def is__phrase__in (phrase, text):
    # See if phrase is present in text
    
    text_lower = text.lower()
    
    for i in string.punctuation:    
        text_lower = text_lower.replace(i, ' ')
        
    text_list = text_lower.split()
    phrase_list = phrase.split()
    
#    print(text_list)
#    print(phrase_list)
    
    indexes = []
    
    for i in range(len(text_list)):
        print(str(text_list[i]))
        if(str(phrase_list[0])==str(text_list[i])):
            indexes.append(i)
    
    print("indexes")
    print(indexes)
    
    for i in indexes:
        match=True
        for j in range(len(phrase_list)):
            try:
                if(str(phrase_list[j])!=str(text_list[i+j])):
                    match=False
            except IndexError:
                return False
        if(match):
            return True
    
    return False

print(is__phrase__in ('hello ok john', 'tub!!! ok!!! john stubby hello'))