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
print("input is", input_string)
open_paren_list = re.findall('\(', input_string)
close_paren_list = re.findall('\)', input_string)

floor = len(open_paren_list) - len(close_paren_list)
print("floor is ", floor, "up ", len(open_paren_list), "down ", len(close_paren_list))
