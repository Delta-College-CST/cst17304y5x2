# This program performs a simple division.  It first
# validates the divisor.

dividend = float(input("Enter dividend: "))
divisor  = float(input("Enter divisor: "))

if divisor != 0:
    quotient = dividend / divisor
    print("Quotient: ", quotient)
else:
    print ("Invalid operation - Divisor cannot be zero.")

