# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:03:23 2016

@author: ericgrimson
"""

x = int(input('Enter an integer: '))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')

v="aeiou"
s="education"
vowels=0
for i in s:
    if i in v:
        vowels=vowels+1;
print("Number of vowels:",vowels)
