# A Simple stone, paper and scissor game

# 0-stone 1-paper 2-scissor

import random
U_choice=int(input("Enter your choice(0/1/2) : "))
C_choice=random.randint(0,2)
if(U_choice>=3 or U_choice<0):
    print("You entered invalid number")

else:
    print(f"your choice = {U_choice} \nComputer choice = {C_choice}")
    if(U_choice == C_choice):
        print("Match is draw")
    elif(U_choice==0 and C_choice==2):
        print("You won the game")
    elif(U_choice==2 and C_choice==0):
        print("You Lost the game")
    elif(U_choice>C_choice):
        print("You won the game")
    else:
        print("You lost the game")
