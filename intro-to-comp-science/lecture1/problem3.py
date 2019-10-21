# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:03:23 2016

@author: subash Pathak
"""

s = 'azcbobobegghakl'
substring='bob'

count=s.count(substring)

print("Number of times bob occurs is:",count)

s = "azcbobobegghakl"
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print ("Longest substring in alphabetical order is:", longest)



# s is predefined variable set to a string value
current = ''
longest = ''
for i in range(len(s)):
 if (s[i] >= s[i-1]):
  current += s[i]
 else:
  current = s[i]
 if len(current) > len(longest):
  longest = current
print("Longest substring in alphabetical order is: " + longest)
