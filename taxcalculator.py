#Tax Calculator - Asks the user to enter a cost and either a
#country or state tax. It then returns the tax plus the total cost with tax.

#imports decimal function to deal with currency
from decimal import *
getcontext().prec = 3

#asks user for cost and tax value, converts input into decimal format
cost = Decimal(raw_input("Please enter the cost of your item: "))
tax = Decimal(raw_input("Please enter the tax rate as a percent: "))/100

#calculates the total and then prints total to console
total = cost +cost*tax
print 'Your total is $',total
