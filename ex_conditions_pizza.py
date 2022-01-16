#Este ejercicio servirá para calcular la cuenta final de las pizzas
#utilizar if, elif, else para ir desarrollandose el codigo

print("Welcome to pizza delivery\n")
size = input("What size of pizza do you want? S, M or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

account_pizza = 0
if size == "S" :
    account_pizza = 15

elif size == "M" :
    account_pizza = 20
    
else:
    account_pizza = 25
    
if add_pepperoni == "Y" :
    if size == "S":
        account_pizza += 2
    else:
        account_pizza += 3

if extra_cheese == "Y" :
    account_pizza += 1

print(f"Your total bill ${account_pizza}")