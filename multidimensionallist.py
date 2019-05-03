#-------------Multidimensional List by Aaron Langley June 2018-----------------
"""
Generate a multiplication table using Multidimensional Lists
"""

import math
import random

#generates table of list
table = [[0] * 10 for i in range(1,10)]

#creates for loops
for i in range(1,10):
    for j in range(1,10):
        table[i][j]= str(i*j)

for i in range(1,10):
    for j in range(1,10):
        print(table[i][j], end=" ")
    print()
