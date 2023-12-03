                 #Enter "report" or "Report" to get the available resource
                 #Enter "off" or "Off" to exit
resource={
    "water":500,
    "milk":500,
    "coffee":100,
    "Money":0

}
menu={
    "Latte":{
       "water":200,
       "milk":100,
       "coffee":24,
       "cost":150
    },

    "Espresso":{
       "water":50,
       "coffee":18,
       "milk":0,
       "cost":100
    },

    "Cappuccino":{
      "water":250,
      "milk":150,
      "coffee":24,
      "cost":200
    },
}

state='on'
def res_check(choice):
    if choice in ['Latte','Espresso','Cappuccino']:
        water=menu[choice]['water']
        milk=menu[choice]['milk']
        coffee=menu[choice]['coffee']
        if resource['water']>=water and resource["milk"]>=milk and resource["coffee"]>=coffee:
            resource["water"]=resource["water"]-water
            resource["milk"]=resource["milk"]-milk
            resource["coffee"]=resource["coffee"]-coffee
            return 1
        else:
            if resource['water']<water:
                print(f"Sorry,there is not enough water")
            elif resource['milk']<milk:
                print(f"Sorry,there is not enough milk")
            elif resource['coffee']<milk:
                print(f"Sorry,there is not enough coffee")
            
    elif choice=='Report': 
        print("Here is the report...😊".center(50));print(f"water & milk-(in ml)✦✧✦ coffee-(in gram)✦✧✦ Money-(in rs) ")
        for i,j in resource.items():
            print(f"{i} : {j}")
     
while (state=='on'):
    choice=input("What would you like to have (Latte/Espresso/Cappuccino) ? ").capitalize()
    if choice=='Off':
        state='Off'
    else:
        check=res_check(choice)
        if check==1:
            print(f"Cost of {choice} is {menu[choice]['cost']}..😊\nPlease enter the coins")
            five=int(input("Enter no_of Rs.5 coins : "))*5
            ten=int(input("Enter no_of Rs.10 coins : "))*10
            twenty=int(input("Enter no_of Rs.20 coins : "))*20 
            total=five+ten+twenty
            cost=menu[choice]['cost']
            if total==cost:
                resource["Money"]=resource["Money"]+total
                print(f"😍 Here is your {choice} 😍")
               
            elif total>cost:
                resource["Money"]=resource["Money"]+cost
                print(f"Here is your Rs.{total-cost} in change")
                print(f"😍 Here is your {choice} 😍")
                
            elif total<cost:
                print("Sorry😞 that's not enough money, Money refunded😊")
