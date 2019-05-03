#Unit Converter (temp, currency, volume, mass and more)
#Converts various units between one another.
#The user enters the type of unit being entered,
#the type of unit they want to convert to and then the value.
#The program will then make the conversion.

#Ask user for measurement type
print("What would you like to convert?",end="")
print()
print("1. Temperature ",end="")
print("2. Volume ",end="")
print("3. Mass ",end="")
print("4. Distance ",end="")
print("5. Pressure ",end="")
print()
choice = int(input("Type number from above: "))

#For temperature option
if(choice == 1):

    #get inout and output along with value
    print()
    print("1. Celcius ",end="")
    print("2. Farenheit ",end="")
    print("3. Kelvin ",end="")
    print()
    unit1 = int(input("Please select the input unit. "))
    value1 = float(input("Please enter the input value. "))
    unit2 = int(input("Please select the output unit. "))

    #convert between F and C
    if(unit1 == 1 and unit2 == 2):
        value2 = (value1*(9.0/5.0)+32)
        print(value1,"F is equal to ",value2,"C")

    #convert between K and C
    elif(unit1 == 3 and unit2 == 1):
        value = (value-273.15)
        print(value1,"K is equal to ",value2,"C")

    #convert between F and K
    elif(unit1 == 2 and unit2 == 3):
        value = ((value-32.0)*(5.0/9.0)+273.15)
        print(value1,"F is equal to ",value2,"K")

    else:
        print("You didn't pick diffferent units...")
        #add bit to restart from top later on

#For volume option
elif(choice == 2):

    #get inout and output along with value
    print()
    print("1. milliliter ",end="")
    print("2. liter ",end="")
    print("3. cubic meter ",end="")
    print("4. cubic inch ",end="")
    print("5. cubic foot ",end="")
    print("6. pint ",end="")
    print("7. quart ",end="")
    print("8. gallon ",end="")
    print("8. barrel ",end="")
    print()
    unit1 = int(input("Please select the input unit. "))
    value1 = float(input("Please enter the input value. "))
    unit2 = int(input("Please select the output unit. "))




#For mass option
#elif(choice == 3):

#For distance option
#elif(choice == 4):

#For pressure option
#elif(choice == 5):

#exception case
#else:
    #print("You didn't pick from the list...")
