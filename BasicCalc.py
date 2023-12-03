#Basic calculator

import os
def  calc(inp1,operation,inp2):
    if operation=="+":
        return inp1+inp2
    elif operation=="-":
        return inp1-inp2
    elif operation=="*":
        return inp1*inp2
    elif operation=="/":
        return inp1/inp2

def new_calc():
    inp1=int(input("Enter the first number : "))
    continue_calc(inp1)

def continue_calc(inp1):
    operation=input("Enter the valid operation (+ , - ,* ,/): ")
    inp2=int(input("Enter the second  number : "))
    result=calc(inp1,operation,inp2)
    print(f"{inp1} {operation} {inp2} ={result}")
    choice=input(f"Enter 'C' to continue calc with {result} or 'N' to start new calc or 'X' to exit: ").upper()
    if choice=='C':
       inp1=result
       continue_calc(inp1)
    elif choice=='N':
        os.system('cls')
        new_calc()
    
new_calc()


