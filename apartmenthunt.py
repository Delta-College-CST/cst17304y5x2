# This program determines an apartment renter's qualifications

# Input
income   = float(input("Monthly income: "))
jobYears = int(input("Years on job: "))
creditScore = int(input("Years credit score: "))

# Determine qualifications for rental.  Write appropriate feedback.
if income > 5000:
    if jobYears > 2:
        print("Accepted - Basic financial qualifications")
    else:
        print("Rejected - Inadequate local work history")
else:
    if creditScore > 700:
        if jobYears > 1: 
            print("Accepted - Basic financial qualifications")
        else:
            print("Rejected - Inadequate work history with credit score")
    else:
        print("Accepted - Inadequate income and credit score")
