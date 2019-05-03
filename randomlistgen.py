#------------Random List Generator by Aaron Langley June 2018------------------
"""
This programs uses the random module to generate random lists of characters
using the random and math libraries. Each list has 5 values.
"""

import math
import random

def random_list(i):
    for i in range (i):
        lst = []
        for num in range(5):
            num = random.randint(0,9)
            lst.append(num)
        print (lst)
        i -+ 1

random_list(5)
