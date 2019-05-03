#####Solve for X by Aaron Langley June 2018###########
"""This programs takes a string and splits it into variable then passes those
variables to solve_x
"""
#x + 4 = 9
#x will always be first variables#will always deal with addition

#defines solve equation
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return "x = " + str(num2 - num1)

print (solve_eq("x + 4 = 9"))
