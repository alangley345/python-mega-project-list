"""
This program generates hex key of whatever length the user specifices
"""

#!/usr/bin/python3
import random
import secrets

while True:

    try:
        keyLength = int(input("How long would you like your key to be? "))
        if (keyLength > 0):
            break

    except ValueError:
        print("Please enter a positive integer")

stringSeed = input("Please enter a seed: ")

seed = list(stringSeed)
print(seed) #debugging


for i in seed:
    seed.append(ord(i))

print(seed) #debugging

seedHex = int(seed.join())
print(seedHex)

key = secrets.token_hex(keyLength)

print(key)
