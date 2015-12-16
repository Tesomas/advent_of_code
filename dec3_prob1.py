'''
Created on Dec 15, 2015

@author: Robert
'''

from sys import argv

script, filename = argv

present_matrix = [[0 for a in range(4000)] for a in range(4000)]
print("here2")
x = 1000
y = 1000
present_matrix[x][y] = 1

file = open(filename)

char_var = file.read(1)

while char_var:
    if char_var == '^':
        y += 1
    elif char_var == 'v':
        y -= 1
    elif char_var == '<':
        x -= 1
    elif char_var == '>':
        x += 1
    
    present_matrix[x][y] += 1
    print(x," ",y)
    char_var = file.read(1)

houses_with_presents = 0

for ctr_1 in range(4000):
    for ctr_2 in range(4000):
        if present_matrix[ctr_1][ctr_2] >= 1:
            houses_with_presents += 1

print(houses_with_presents)
        



