from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

menus = Menu()
menu_item = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

#Print report

coffee_machine.report()
money_machine.report()


#Check if resources are available

drink = menus.find_drink('latte')
coffee_machine.is_resource_sufficient(drink)


#Procesar las monedas

report = money_machine.report()
pago = money_machine.make_payment(2.5)

#Hacer cafe

result = coffee_machine.make_coffee(drink)