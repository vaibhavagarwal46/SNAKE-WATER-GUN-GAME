import random


print("Type SNAKE, WATER, or GUN")
print("Type Q to quit the game\n")

youDICT = {
    "SNAKE": 1,
    "WATER": -1,
    "GUN": 0
}

reverseDICT = {1: "SNAKE", -1: "WATER", 0: "GUN"}

while True:
    computer = random.choice([-1, 1, 0])

    youchoice = input("Enter your choice: ").upper()

    if youchoice == "Q":
        print("Thanks for playing")
        break

    if youchoice not in youDICT:
        print("Invalid choice... Please enter SNAKE, WATER, or GUN.")
        continue

    you = youDICT[youchoice]

    print(f"You chose {reverseDICT[you]}")
    print(f"Computer chose {reverseDICT[computer]}")

    if computer == you:
        print("It's a draw!\n")
    else:
        if (computer == -1 and you == 1) or \
           (computer == 1 and you == 0) or \
           (computer == 0 and you == -1):
            print(" You win!\n")
        else:
            print(" You lose!\n")
