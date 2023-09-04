# This program demonstrates a basic set of if-statements

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#-------------------------

# Determine relationship between the two numbers
if a == b:
    print("a == b")
if a > b:
    print("a > b")
if a < b:
    print("a < b")

#-------------------------

if a == b:
    print("a == b")
else:
    if a > b:
        print("a > b")
    else:
        print("a < b")

#-------------------------

if a == b:
    print("a == b")
elif a > b:
    print("a > b")
else:
    print("a < b")

#-------------------------
