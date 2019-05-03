#Find Cost of Tile to Cover W x H Floor
#Calculate the total cost of tile it would take to cover a floor plan
#of width and height, using a cost entered by the user.

import decimal

#get length, width and cost from the user
floor_length = input("How long is the room in decimal feet? ")
floor_width = input("How wide is the room in decimal feet? ")
floor_cost = input("How much does the flooring cost per square foot? ")

#convert inputs to floats
floor_length = float(floor_length)
floor_width = float(floor_width)
floor_cost = float(floor_cost)

#total for the project
total_cost = decimal.Decimal((floor_length)*(floor_width)*(floor_cost))

#prints cost out the user
print("Your floor will cost $",round(total_cost,2g),"")
