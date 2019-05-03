####################Find Prime by Aaron Langley June 2018######################
"""
This program takes a user input and finds the primes up to and including input
"""
#loop through input deincrementing by one and dividing through
def find_prime(num):
    for num in range(2,num+1):
        prime = True
        for i in range(2,num):
            if num % i ==  0:
                prime = False

        if prime:
            print (num)

#prompt user for input
print ("Welcome to Find Prime!")

#exception loop
while True:
    try:
        num = int(input("Please enter a positive integer greater than 1: "))
        if num > 1: #runs actual function
            find_prime(num)
            break
        else:
            print ("Oops! That is not a valid input...")

    except ValueError:
        print ("Oops! That is not a valid input...")
