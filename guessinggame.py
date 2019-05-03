#Guessing Game by Aaron Langley June 2018

#import random module
import random

#create random integer
random = random.randint(1,10)

#test random
print (random)

while True:

    try:
        #prompt user for a number between 1 and 10
        guess = int(raw_input("Please guess an integer between 1 and 10: "))


        #guessed correctly
        if guess == random:
            print("You guessed correctly!")
            break

        #guess outside range
        elif guess < 1 or guess > 10:
            print("You didn't enter an integer between 1 and 10...")

        #if guess is incorrect
        else:
            print("You're wrong!")

    #value error
    except ValueError:
        print("Invalid input...")
