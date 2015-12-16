'''
Created on Dec 15, 2015

@author: Robert
'''
import re
from sys import argv

def check_good(line):
    match1 = re.search(r"([A-z])(\w)\1", line)
    if match1:
        match = re.search(r"([A-z][A-z]).*\1", line)
        if match:
            print(line)
            return True
    return False


script, filename = argv

file = open(filename)
text_lines = file.readlines()
ctr = 0
for line in text_lines:
    if check_good(line):
        print(line)
        ctr += 1

print(ctr)
    


