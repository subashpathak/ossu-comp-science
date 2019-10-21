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

word="bob"
s='azcbobobegghakl'
for i in s:
    if i in word:
        word=word+1;
print("Number of times bob occurs is:",word)


# variable s is predefined
# define and set variable vowelCount to 0
vowelCount = 0
# create a for loop to iterate through each character of s
for letter in s:
    # if letter in s equal to each vowel, increment vowelCount by 1
    if letter == "a":
        vowelCount += 1
    elif letter == "e":
        vowelCount += 1
    elif letter == "i":
        vowelCount += 1
    elif letter == "o":
        vowelCount += 1
    elif letter == "u":
        vowelCount += 1
# print the concatenated first string and vowelCount
print("Number of vowels: " + str(vowelCount))

#https://medium.com/cyberdoggo/mit-6-00-1x-problem-set-1-c5ba79ae2aad
