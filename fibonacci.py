#Fibonacci Sequence
#Enter a number and have the program generate the Fibonacci
#sequence to that number or to the Nth number.

#creates a Fibonacci function
def fibonacci(n):

    #creates list to print
    f =[]
    a,b = 0,1

    #while loop
    while b < n:
        f.append(b)
        a,b = b,(a+b)

    #prints a list
    print f

i = input("Enter a number: ")
fibonacci(i)
