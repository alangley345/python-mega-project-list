#Happy Numbers - A happy number is defined by the following process.
#Starting with any positive integer, replace the number by the sum of the
#squares of its digits, and repeat the process until the number equals 1
#(where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy numbers, while those
#that do not end in 1 are unhappy numbers.
#Display an example of your output here. Find first 8 happy numbers.

#!/usr/bin/python3

from multiprocessing import Process
import os

def squared(list):
    #enumerates through list and ssquares each value
    for i,value in enumerate(list):
        j = int(value)**2
        list.remove(value)
        list.insert(0,j)

def happy():
    happy = []
    number = 1

    while len(happy) < 8:

        lst = list(str(number))

        count = 0

        while count < 5000:

            squared(lst)
            result = sum(lst[0:len(lst)])
            print(result)

            if result == 1:
                happy.append(number)
                break

            else:
                del lst[:]
                lst = list(str(result))
                count += 1

        number += 1

    print(happy)

processes = [ ]

for i in range(os.cpu_count()):
    print('registering process %d' % i)
    processes.append(Process(target=happy))

for process in processes:
    process.start()

for process in processes:
    process.join()
    
print("Done!")
