# This program calculates the cost for a catering event

# Prompt for input.
headcount = int(input("Enter number people attending: "))
                
# If not valid, provide specific message.
# Otherwise, determine unit cost for given count.
if headcount <= 0:
    print("Invalid input.")
elif headcount > 200:
    print("Count too large.")
else:
    if headcount <= 20:
        unitCost = 150
    elif headcount <= 50:
        unitCost = 130
    elif headcount <= 100:
        unitCost = 110
    else:
        unitCost = 100

    # Calculate cost
    cost = unitCost * headcount

    # Display output report
    print()
    print("CATERING ORDER")
    print("Serving:",headcount, "| Cost: $%8.2f" % (cost))
