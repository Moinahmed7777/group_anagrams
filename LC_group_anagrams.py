# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 18:03:06 2020

@author: Necro
"""


strs=["eat", "tea", "tan", "ate", "nat", "bat"]
hashmap = {}
for st in strs:
    key = ''.join(sorted(st))
    
    if key not in hashmap:
        hashmap[key] = [st]
    else:
        hashmap[key] += [st]
print( hashmap.values())
    