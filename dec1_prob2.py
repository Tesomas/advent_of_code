'''
Created on Dec 13, 2015

@author: Robert
'''
import re
from sys import argv
from sys import argv
 
script, filename = argv

file = open(filename);
input_string = file.read()
print(input_string)
split_list = re.split("(.)", input_string)
#print(split_list)
floor = 0
ctr = 1
for item in split_list:
    print(item)
    if item == "(":
        floor += 1
        ctr += 1
    elif item == ")":
        floor -= 1
        ctr +=1
    
    if floor == -1 :
        print("ctr is ", ctr, "len is ",len(split_list))
        break
        