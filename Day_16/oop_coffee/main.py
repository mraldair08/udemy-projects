from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu_item = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    order_name = input(f"What would you like? ({menu_item.get_items()}): ").lower()
    if order_name == 'off':
        is_on = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item.find_drink(order_name)
        print(order_name)