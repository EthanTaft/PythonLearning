# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:32:48 2017

@author: Ethan
"""

mydict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
event = 2
for k in list(mydict.keys()):
    if k == event:
        del(mydict[k])
        
mydict

def remove(diction):
    event = 2
    for k in list(diction.keys()):
        if diction[k] == event:
            del(diction[k])
    return(diction)
    
remove(mydict)

del(mydict[2])

list(mydict.keys())