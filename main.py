from Coffe_Machine_Resources import menu
from Coffe_Machine_Resources import resources

money=0
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
#TODO 1   choice drink
def actions():
    drink=input("What would you like? (espresso/latte/cappuccino/report)")
    if drink=="report":
        print(resources["water"],"ml of water")
        print(resources["milk"],"ml of milk")
        print(resources["coffee"],"mg of coffee")
        print (money,"money in")

        return False

    if drink=="espresso":
        return drink
    elif drink=="latte":
        return drink
    elif drink=="cappuccino":
        return drink

#TODO 2 check resources sufficient
def availability(drink):
    if drink==False:
        pass
    elif drink =="espresso":
        if resources["water"] >= menu[drink]["ingredients"]["water"]:
            if resources["coffee"] >= menu[drink]["ingredients"]["coffee"]:
                return True
        print("Sorry there are not enough resources for making your coffee,try again later!")
        return False

    else:

        if resources["water"] >= menu [drink]["ingredients"]["water"]:
            if resources["milk"] >= menu[drink]["ingredients"]["milk"]:
                if resources["coffee"] >= menu[drink]["ingredients"]["coffee"]:
                    return True
        print("Sorry there are not enough resources for making your coffee,try again later!")
        return False

#TODO 3 process coins
def pay():
    print("Please insert coin")
    quarters_n=float(input ("How many quarters"))
    quarters_n=quarters_n*quarters
    dimes_n = float(input("How many dimes"))
    dimes_n=dimes_n*dimes
    nickles_n = float(input("How many nickles"))
    nickles_n=nickles_n*nickles
    pennies_n=float(input("How many pennies?"))
    pennies_n=pennies_n*pennies
    tot=quarters_n+dimes_n+nickles_n+pennies_n

    return tot

#TODO 4 check transaction is successful
def check_transaction(tot,drink):
    if tot>menu[drink]["cost"]:
        cashback=tot-(menu[drink]["cost"])
        print(f"Here is {cashback} in change")
        gain=tot-cashback
        return gain
    else:
        print("Not enough money inserted,try again")
        return False

#TODO 5 update resources
def storage(drink):
    materials=dict()
    if drink=="espresso":
        materials["water"]=(resources["water"]) - (menu[drink]["ingredients"]["water"])
        materials["coffee"]=(resources["coffee"]) - (menu[drink]["ingredients"]["coffee"])
        materials["milk"]=resources["milk"]
    else:
        materials["water"] = (resources["water"]) - (menu[drink]["ingredients"]["water"])
        materials["coffee"] = (resources["coffee"]) - (menu[drink]["ingredients"]["coffee"])
        materials["milk"] = (resources["milk"]) - (menu[drink]["ingredients"]["milk"])

    return materials


#TODO 6 profit(gain)
def profit(gain,money):
    money=money + gain
    return money


#TODO 7 make coffee
def enjoy(coffee):
    print("Here is your coffee, enjoy!")
    return True


while True:
    drink=actions()
    if drink==False:
        pass
    else:
        check=availability(drink)
        if check==False:
            break
        else:
            tot=pay()
            gain=check_transaction(tot,drink)
            if gain==False:
                gain
            else:
                resources=storage(drink)
                money=profit(gain,money)
                made=enjoy(drink)

print(f"Total resources={resources},total profit today= {money}")












