import random

computer = random.choice([-1 , 1 ,0])


youchoice = input("Enter your choice( SNAKE , WATER or GUN ): ")
youDICT = {
    "SNAKE" : 1 ,
     "WATER" : -1 , 
     "GUN" : 0
     } 
you = youDICT[youchoice]
reverseDICT = { 1 : "SNAKE" , -1 : "WATER" , 0 : "GUN"}

print(f"You chose {reverseDICT[you]} \nComputer chose {reverseDICT[computer]}")

if(computer == you):
    print ("its a draw")

else:
    if (computer == -1 and you == 1):
        print("You win")
    elif (computer == -1 and you == 0):
        print ("You lose ")    
    elif (computer == 1 and you == -1):
        print ("You lose ")
    elif (computer == 1 and you == 0):
        print ("You win ")   
    elif (computer == 0 and you == -1):
        print ("You win ")   
    elif (computer == 0 and you == 1):
        print ("You lose ")    
    else:
        print ("Something went wrong")         


