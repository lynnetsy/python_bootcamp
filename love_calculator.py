#Vamos a crear un love calculator pidiendo el nombre de dos personas
#y contanto en los nombres de estas personas cuantas veces se repite TRUE 
#sumarlo, luego hacemos lo mismo con LOVE y vamos a combinar el valor total de TRUE con LOVE
#EJEMPLO obtenemos que en true sumando los 2 nombres tenemos 6 y en love se obtiene sumando en los 2 nombres
#tendremos un %62 de compatibilidad

print("Welcome to love calculator\n")
name_1 = input("Introduce el nombre de la persona:\n")
name_2 = input("Introduce el nombre de la otra persona:\n")

lower_name_1 = name_1.lower()
lower_name_2 = name_2.lower()

count_true = 0
count_love = 0

for letra in "true":
    count_true += lower_name_1.count(letra)
    count_true += lower_name_2.count(letra)

for letra in "love":
    count_love += lower_name_1.count(letra)
    count_love += lower_name_2.count(letra)

result = int(f"{count_true}{count_love}")
percent_compatibility = (f"you have {result}% of compatibility ")

print(percent_compatibility)

if result < 10 or result > 90 :
    print(f"Your score is {result} you go together like coke and mentos")
elif result >= 40 and result <= 50:
    print(f"Your score is {result} you are alright together")
else:
    print(f"your score is {result}") 