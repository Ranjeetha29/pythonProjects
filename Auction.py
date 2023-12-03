
# A simple Silent auction Program

print("****************************************************");print("✹✹✹ Silent Aution Program ✹✹✹".center(50));print("****************************************************")
import os
def find_winner(Aution):
    max=0
    for i,j in Aution.items():
       if j>max:
         max=j
         name=i
    print(f"The winner is {name} with a bid of {max}")
Aution={}

choice="Yes"
while(choice!="No"):
    name=input("What's your name? ")
    Bid_Price=int(input("What's your bid price?"))
    Aution[name]=Bid_Price
    choice=input('Are there any other bidders("Yes" or "No")? ').capitalize()
    os.system('cls')
find_winner(Aution)

