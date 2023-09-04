# This program creates a simple banking menu.  It assumes a
# $1000 starting balance and allows a deposit or withdrawal.
# Withdrawals cannot exceed current balance.  A third option
# adds a 1% interest to the balance.

balance = 1000.00      # Initial balance
INTEREST_RATE = 0.01   # Current interest rate for account

# Display menu and accept menu selection
print("BANK of DELTA")
print("1: Deposit")
print("2: Withdrawal")
print("3: Add Interest")
selection = int(input("Enter Selection: "))




  # ENTER YOUR CODE HERE




# For all transactions, display final balance
print("Balance now: $%8.2f" % (balance))
				

