#A Random Password Generator

import random
print("****************************************************");print("Welcome to password generator!".center(50));print("****************************************************")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['@','#','$','&','*','!','^']

l_count=int(input("Enter number of letters needed in password: "))
n_count=int(input("Enter number of numbers needed in password: "))
s_count=int(input("Enter number of symbols needed in password: "))
password_list=[]
for i in range(1,l_count+1):
    password_list+=random.choice(letters)
for i in range(n_count):
    password_list+=random.choice(numbers)
for i in range(s_count):
    password_list+=random.choice(symbols)

random.shuffle(password_list)
Password=""
for ch in password_list:
    Password+=ch
print(f"Your Password is {Password}".center(48))
print("****************************************************")
