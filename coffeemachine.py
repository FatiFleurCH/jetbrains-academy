# Write your code here
money = 550
water = 400
milk = 540
coffee = 120
cups = 9

class CoffeeMachine:
    def __init__(self, money, water, milk, coffee, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.available = {
            "water" : self.water,
            "milk" : self.milk,
            "coffee beans": self.coffee,
            "disposable cups": self.cups,
            "money": self.money,
        } 
    def main(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        while action != "exit":
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    def fill(self):
        self.water += int(input('Write how many ml of water the coffee machine has:\n'))
        self.milk += int(input('Write how many ml of milk the coffee machine has:\n'))
        self.coffee += int(input('Write how many grams of coffee beans the coffee machine has:\n'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    def take(self):
        print(f"I gave you ${money}")
        self.money = 0
        
    def remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
        
    def buy(self):
        coffee_type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        espresso = {
            "money": 4,
            "water": 250,
            "milk": 0,
            "coffee beans": 16,
            "disposable cups": 1
        }
        latte = {
            "money": 7,
            "water": 350,
            "milk": 75,
            "coffee beans": 20,
            "disposable cups": 1
        }
        cappuccino = {
            "money": 6,
            "water": 200,
            "milk": 100,
            "coffee beans": 12,
            "disposable cups": 1
        }
        drinks = {
            '1': espresso,
            '2': latte,
            '3': cappuccino
        }
        def make_drink(coffee_type):
            if self.water < drinks[coffee_type]["water"]:
                print("Sorry, not enough water!")
            elif self.milk < drinks[coffee_type]["milk"]:
                print("Sorry, not enough milk!")
            elif self.coffee < drinks[coffee_type]["coffee beans"]:
                print("Sorry, not enough coffee beans!")
            elif self.cups < drinks[coffee_type]["disposable cups"]:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.money += drinks[coffee_type]["money"]
                self.water -= drinks[coffee_type]["water"]
                self.milk -= drinks[coffee_type]["milk"]
                self.coffee -= drinks[coffee_type]["coffee beans"]
                self.cups -= drinks[coffee_type]["disposable cups"]
        if coffee_type == '1':
            make_drink(coffee_type)
        elif coffee_type == '2':
            make_drink(coffee_type)
        elif coffee_type == '3':
            make_drink(coffee_type)


        

    

coffe_machine = CoffeeMachine(money, water, milk, coffee, cups)
coffe_machine.main()

