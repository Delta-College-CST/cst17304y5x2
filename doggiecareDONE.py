# This program inputs a dog's name and weight.  It calculates and
# displays the weekly rate for day care based on the dog's weight.

# Prompt for info on dog
name   = input("Enter dog's name: ")
weight = float(input("Enter dog's weight: "))

# Calculate weekly cost for care - based on weight
if weight < 15:
    cost = 55
elif weight <= 30:
    cost = 75
elif weight <= 80:
    cost = 105
else:
    cost = 125

# Write summary
print("To care for",name,"the weekly rate is $",cost)
