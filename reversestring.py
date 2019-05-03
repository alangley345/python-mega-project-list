#Reverse a String - Enter a string and the program
# will reverse it and print it out.

#generates a single entry in a list
word = list(raw_input("Enter a word: "))

#reverses the list
word.reverse()

#print the list
print "".join(word)
