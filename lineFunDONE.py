# The program performs the operation y = 3x - 5, but only on negative numbers

x = int(input("Enter x: "))  # Input x

if x < 0:                    # If x is negative
    y = 3 * x - 5                # Calculate y
    print("y: ",y)               # Output y
else:
    print("Input error")     # Otherwise, error msg
