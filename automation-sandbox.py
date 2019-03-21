#!/usr/bin/env python
# coding: utf-8

# # Regular Expression (regexes)
# Find patterns of text with regular expression, *regexes* <br>
# Resources: Automate Boring Stuff with Python
# 1. Find simple phone number in string without regrexes
# 2. Use regrexes to detect simple phone number
# 3. Group with parentheses and match multiple groups with pipe
# 4. Optional match with question mark

# In[2]:


import pandas as pd
import numpy as np
import re
import os
os.getcwd()


# ## 1. Use function to detect simple phone number 
# - For simplicity, we only test the 000-000-0000 phone number format
# - `isPhoneNum` function applies to str type, so it does not work for sentence in str type 
# - `findPhoneNum` function can try to get the phone number from a sentence str

# In[5]:


def isPhoneNum(text):
    # Filter out the string that is longer than a phone number
    if len(text) != 12:
        return False
    
    # Filter out the strings that contain letters 
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    
    # Filter out the strings with no hyphen at the 4th and 8th digit
    if text[3] != '-' or text[7] != '-':
        return False
    
    return True

print('345-231-4587 is a phone number:')
print(isPhoneNum('345-231-4587'))
print('moshi moshi is a phone number:')
print(isPhoneNum('moshi moshi'))


# In[8]:


def findPhoneNum(message):
    for i in range (len(message)):
        chunk = message[i:i+12]
        if isPhoneNum(chunk):
            print(f'Phone number detected: {chunk}')
    
line_1 = 'Is 347-264-8562 your phone number?'
line_2 = '897-124-3745 is a stranger number'

findPhoneNum(line_1)
findPhoneNum(line_2)


# ## 2. Detect phone number with regexes
# - `import re` to get the module for regular expression
# - `\d`: stands for digit character
# - `{n}`: added after a pattern to match the pattern n times
# - `re.compile()`: creates regex objects `ro`
# - `ro.search('string')`: matches the regex objects within any strings
# - `mo.group()`: returns the matched text from searched string

# In[19]:


phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
match_object = phone_regex.search('My number is 484-362-3678')
print(match_object)
print(f'Using mo.group() method we get: {match_object.group()}')


# 
