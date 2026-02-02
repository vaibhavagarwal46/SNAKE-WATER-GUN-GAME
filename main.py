import random

computer = random.choice([-1, 1, 0])

youchoice = input("Enter your choice (SNAKE, WATER or GUN): ").upper()

youDICT = {
    "SNAKE": 1,
    "WATER": -1,
    "GUN": 0
}

reverseDICT = {1: "SNAKE", -1: "WATER", 0: "GUN"}

if youchoice not in youDICT:
    print("Invalid choice! Please choose SNAKE, WATER, or GUN.")
else:
    you = youDICT[youchoice]

    print(f"You chose {reverseDICT[you]}")
    print(f"Computer chose {reverseDICT[computer]}")

    if computer == you:
        print("It's a draw")
    else:
        if (computer == -1 and you == 1) or \
           (computer == 1 and you == 0) or \
           (computer == 0 and you == -1):
            print("You win")
        else:
            print("You lose")
