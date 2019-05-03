#--------------------Bubble Sort by Aaron Langley June 2018---------------------
"""
This uses two loops to effciently sort a list of values
"""
import math
import random

numList = []
for i in range (5):
    numList.append(random.randrange(1,10))

i = len(numList) - 1

while i > 1:

    j = 0

    while j < i:
            if numList[j] > numList[j+1]:

                temp = numList[j]
                numList[j] = numList[j + 1]
                numList[j + 1] = temp

            else:
                print()

            j += 1

    i -= 1

for k in numList:
    print(k,end="")
print()
