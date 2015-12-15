'''
Created on Dec 14, 2015

@author: Robert
'''
import re
from sys import argv

def ribbon_calc(a,b):
    return 2*a + 2*b
    
script, filename = argv

file = open(filename)

input_string = file.read()

string_list = re.split('\n', input_string)

total_ribbon_len = 0

for lwh in string_list:
    if lwh == "":
        break
    value_list = re.findall('\d+', lwh)
    l = int(value_list[0])
    w = int(value_list[1])
    h = int(value_list[2])
    ribbon_len = 0
    if l <= h and w <= h:
        ribbon_len = ribbon_calc(l,w)
    elif l <= w and h <= w:
        ribbon_len = ribbon_calc(l,h)
    else:
        ribbon_len = ribbon_calc(w,h)
    print(ribbon_len, l*w*h)
    ribbon_len += l*w*h
    print(ribbon_len)
    total_ribbon_len += ribbon_len
    
print(total_ribbon_len)
