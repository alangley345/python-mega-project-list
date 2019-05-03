#prints a welcome screen
print "Welcome to Pig Latin Translator"

#asks the user for their word and turns it into a list
word = list(raw_input("Enter a word to translate: "))

#pulls first character from list and stores it in new
new = word.pop(0)

#appends the list with the value new and 'ay' / prints result to screen
word.append(new+'ay')
print "".join(word)
