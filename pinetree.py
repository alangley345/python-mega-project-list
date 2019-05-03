#ask user how tall the tree is
height = input("How tall is the tree? ")
height = int(height)
stump = height - 1
spaces = height - 1
hashes = 1

#create while statement for input, loops until height = 1
while (height != 0):

#prints spaces for each increment
    for i in range (spaces):
        print(' ',end="")

#print the hashes for branches
    for i in range (hashes):
        print('#',end="")

#new line
    print()

#deincrement spaces
    spaces -= 1

#deincrement hashes
    hashes += 2

#deincrement height
    height -= 1

#print stump spaces
for i in range (stump):
    print(" ",end="")

print("#")
