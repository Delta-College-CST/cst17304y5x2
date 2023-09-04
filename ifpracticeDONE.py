# CST 173 if-Statement Practice

#################################################

score = int(input("Enter score: "))

# If score is 100 or over, add 10 points
if score >= 100:
    score = score + 10
    
print ("Score: ",score)
print ()

#################################################

orderTotal = float(input("Enter total order ($): "))

# If total for order over $200, shipping is $20
# Otherwise, shipping is 10% of order cost.
if orderTotal > 200.00:
    shipping = 20.0
else:
    shipping = 0.10 * orderTotal

total = orderTotal + shipping

print ("Total order: $",total)
print ()

#################################################






