#have the user enter their investment amount and interest
deposit = input("Please enter your deposit: ")
interest = input("Please enter the interest rate: ")
deposit = float(deposit)
interest = float(interest*0.01)

#Each year the amount will increase by their investment + invesdtment * interest
for deposit in range (10):
	deposit = deposit + (deposit * interest) 
	print (deposit)

#Print out return after 10 years
print("Your deposit will be: ${:.2f}".format(deposit))