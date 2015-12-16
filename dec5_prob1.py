'''
Created on Dec 15, 2015

@author: Robert
'''

import re
from sys import argv

def check_good(line):
    vowels = re.findall("[aeiou]", line)
    if len(vowels) >= 3:
        
        match = re.search(r"([A-z])\1", line)
        
        if match:
            print(line)
            return True
    return False

def check_not_bad(line):
    match = re.search("ab|cd|pq|xy", line)
    if match:
        return False
    return True


script, filename = argv

file = open(filename)
text_lines = file.readlines()
ctr = 0
for line in text_lines:
    if check_good(line):
        print(line)
        if check_not_bad(line):
            ctr += 1

print(ctr)
    


