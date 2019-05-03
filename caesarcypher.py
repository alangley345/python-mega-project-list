"""Caesar Cypher by Aaron Langley June 2018
this programs creates crypto via shifting values in unicode. It is not an
effective cypher since it is frequency dependent.
"""

#prompts user for input
msg = input("Please enter you message: ")
key = int(input("Please enter a key between 1 and 10: "))
uncoded = []
coded = []

#defines the crypto function
def caesar(lst,key):
    for n,i in enumerate(lst):
        if i != 32:
            lst[n] = lst[n]-key
        else:
            lst[n] = lst[n]

#turns message into a list
for char in msg:
    uncoded.append(char)

#items in  list to ascii values
for item in uncoded:
    coded.append(ord(item))

#shift items over key spaces
caesar(coded,key)

#clears uncoded list
del uncoded[:]

#prints coded message
for item in coded:
    uncoded.append(chr(item))

#decode message and print
caesar(coded,-key)

print (coded) #for debugging only
print (uncoded) #for debugging only

"""
#print decoded message
print ("".join(str(x) for x in decoded))
"""
