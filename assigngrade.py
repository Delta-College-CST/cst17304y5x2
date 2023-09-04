# This program averages three test scores, determines
# if a student is passing or failing, and assigns
# a letter grade

# Input two numbers
test1 = int(input("Enter Test 1 score: "))
test2 = int(input("Enter Test 2 score: "))
test3 = int(input("Enter Test 3 score: "))

# Calculate test average
average = (test1 + test2 + test3) / 3.0

# Write test average and determine if student's grade will
# transfer to a university.
print()
print("Test Average: ",average)
if average >= 73.0:
    print("TRANSFER OK")
else:
    print("TRANSFER ISSUES")

# Wite letter grade
print("with a grade of:")
if average >= 90.0:
    print("A")
elif average >= 80.0:
    print("B")
elif average >= 70.0:
    print("C")
elif average >= 60.0:
    print("D")    
else:
    print("F")
    
########################################################


