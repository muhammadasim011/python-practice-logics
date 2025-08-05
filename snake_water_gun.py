import random

"""
snake  1
water -1
gun    0
"""

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s/w/g): ").lower().strip()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr not in youDict:
    print("Invalid input! Choose 's', 'w', or 'g'.")
    exit()

you = youDict[youstr]
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It’s a draw!")
elif (computer == -1 and you == 1) \
     or (computer == 1  and you == 0) \
     or (computer == 0  and you == -1):
    print("You win!")
else:
    print("You lose!")
