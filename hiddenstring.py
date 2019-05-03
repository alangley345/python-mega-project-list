#Hidden String by Aaron Langley June 2018
#receive a string and convert it to ascii and back with print statements

#user inputted message
message  = raw_input("Please enter your message: ")

#creates blank lists
plain_list = []
secret_list = []

#converts string to list of characters
for char in message:
    plain_list.append(char)

#cycles through plain_list generating ints using ord()
for item in plain_list:
    secret_list.append((ord(item)))

#prints hidden message without formatting
print ("Your secret message is:\n" +"".join(str(x) for x in secret_list))

#deletes contents of plain_list
del plain_list[:]

#converts list of ascii into characters
for item in secret_list:
    plain_list.append(chr(item))

#print original message without formatting
print ("Your original message was:\n"+"".join(plain_list))
