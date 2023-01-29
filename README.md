This script simulates a coffee vending machine. 

It has several functions that are called in a loop to simulate the process of making a coffee.

The first function, actions(), prompts the user to input the type of coffee they would like to order.
If the user inputs "report", it prints out the current resources of water, milk, and coffee in the machine. 
If the user inputs "espresso", "latte", or "cappuccino", it returns the user's choice of drink.

The second function, availability(drink), checks if there are enough resources to make the coffee based on the user's choice of drink. 
It compares the resources of water, milk, and coffee to the ingredients needed to make the selected drink.
If there are enough resources, it returns True, otherwise it prints a message saying there aren't enough resources and returns False.

The third function, pay(), prompts the user to insert coins in quarters, dimes, nickles, and pennies.
It converts the number of each coin to its corresponding monetary value and returns the total amount paid.

The fourth function, check_transaction(tot,drink), compares the total amount paid to the cost of the selected drink.
If the total amount paid is greater than the cost of the drink, it calculates the change and returns the amount of money gained by the machine.
If the total amount paid is less than the cost of the drink, it prints a message saying there isn't enough money and returns False.

The fifth function, storage(drink), updates the resources by subtracting the ingredients used to make the selected drink from the current resources.

The sixth function, profit(gain,money), adds the amount of money gained from the transaction to the current profit of the machine.

The seventh function, enjoy(coffee), prints a message saying "Here is your coffee, enjoy!" and returns True.

The script then enters a while loop, where each of these functions is called in succession. 
The loop continues until the user inputs "report" or the availability() function returns False. 
At the end of the loop, the script prints the total resources and the total profit of the machine.



