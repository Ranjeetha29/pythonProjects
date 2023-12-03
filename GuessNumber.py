print("****************************************************");print("★ ☆ ★ ☆ GUESS THE NUMBER ☆ ★ ☆ ★  ".center(50));print("****************************************************")
import random

def guess_num(i,number):
     while(i>=1):
        guess=int(input("Enter your guess : "))
        if guess==number:
            print(f"Your answer is right ...The number is {number}♔ ")
            break
        elif guess<number:
            print("your guess is too low")
        else:
             print("your guess is too high")
             
        if i==1:
            print(f"You have no attempts ....You lost the game")    
        else:
            print(f"You have only {i-1}  attempts\n ")
        i-=1

number=random.randint(1,20)
level=input("Enter the level ('E'  for Easy or 'H' for Hard) : ").upper()
if level=='E': 
    i=10
    guess_num(i,number)

if level=='H':
    i=5
    guess_num(i,number)
    
