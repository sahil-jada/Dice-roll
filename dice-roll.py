import random
print("Welcome to the dice roll game")
x = input("Enter 'y' to roll the dice: ")
while x == 'y':
    roll = random.randint(1,6)
    if roll == 1:
        print("---------")
        print("|       |")
        print("|  ⚫   |")
        print("|       |")
        print("---------")

    elif roll == 2:
        print("---------")
        print("|⚫     |")
        print("|       |")
        print("|     ⚫|")
        print("---------")

    elif roll == 3:
        print("---------")
        print("|⚫     |")
        print("|   ⚫  |")
        print("|     ⚫|")
        print("---------")

    elif roll == 4:
        print("---------")
        print("|⚫   ⚫|")
        print("|       |")
        print("|⚫   ⚫|")
        print("---------")

    elif roll == 5:
        print("---------")
        print("|⚫   ⚫|")
        print("|   ⚫  |")
        print("|⚫   ⚫|")
        print("---------")

    elif roll == 6:
        print("---------")
        print("|⚫⚫⚫|")
        print("|       |")
        print("|⚫⚫⚫|")
        print("---------")

    x = input("Roll again? y/n: ")
    if x != 'y':
        print("Thankyou for playing")
        break
