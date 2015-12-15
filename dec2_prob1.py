'''
Created on Dec 14, 2015

@author: Robert
'''
import re
from sys import argv

script, filename = argv

file = open(filename)

input_string = file.read()

string_list = re.split('\n', input_string)

total_sq_ft = 0

for lwh in string_list:
    if lwh == "":
        break
    value_list = re.findall('\d+', lwh)
    l = value_list[0]
    w = value_list[1]
    h = value_list[2]
    print(l, "x", w, "x", h)
    side_1 = int(l)*int(w)
    side_2 = int(w)*int(h)
    side_3 = int(h)*int(l)
    smallest_side = min(side_1, side_2, side_3)
    pres_sq_ft = (2*side_1) + (2*side_2) +(2*side_3) + smallest_side
    total_sq_ft += pres_sq_ft
    print(pres_sq_ft)

print(total_sq_ft)


