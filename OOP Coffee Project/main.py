from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()




loop = True
while loop:
    coffee = input(f"what type of coffee would you like {menu.get_items()}:  ")
    if coffee == "off":
        loop = False
    elif coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_item = menu.find_drink(coffee)
        if coffee_maker.is_resource_sufficient(coffee_item) and money_machine.make_payment(coffee_item.cost):
                coffee_maker.make_coffee(coffee_item)

        # cost = get_cost(coffee_item)
        # resources_item = resources(coffee_item)
        # if resources_item:
        #     if make_payment(cost):
        #         CoffeeMaker().make_coffee(coffee_item)


# coffee_maker = CoffeeMaker()
# money_machine = MoneyMachine()
# menu = Menu()
#
#
# coffee = input(f"what type of coffee would you like {menu.get_items()}: ")
# coffee_item = menu.find_drink(coffee)
# coffee_maker.report()
# money_machine.report()
# coffee_maker.is_resource_sufficient(coffee_item)
# money_machine.make_payment(coffee_item.cost)
# coffee_maker.make_coffee(coffee_item)



