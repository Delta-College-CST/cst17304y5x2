# This program simulates drawing a card (though not
# exactly realistically form a deck of cards)

import random 

cardNum = random.randint(1, 13)

if cardNum == 1:
    print("Ace")
elif cardNum == 11:
    print("Jack")
elif cardNum == 12:
    print("Queen")
elif cardNum == 13:
    print("King")
else:               # For card faces 2..10
    print(cardNum)
