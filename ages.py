#if age is 5, go to kindergarten
#Ages 6 to 17 go to grades 1 thru 12
#If age is greater than 17, go to college
#less than 10 lines

#Ask user for their age
age = input("Enter age: ")
age = int(age)

#<5
if (age <5):
	print("Too young for school")	

#5
elif (age == 5):
	print("Go to kindergarten")

#6-17
elif (age > 5 and age < 18):
	age = str (age-5)
	print("Go to grade " + age)
#>17
else:
	print("Go to college")